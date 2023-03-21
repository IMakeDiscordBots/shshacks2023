<script>
    export let fileInput = null;
    import * as tf from "@tensorflow/tfjs";
    /**
     * @type {string}
     */
    let percentage;
    /**
     * @type {any[]}
     */
    let selectedFiles = [];

    /**
     * @param {{ preventDefault: () => void; }} event
     */
    function handleDragOver(event) {
        event.preventDefault();
    }
    /**
     * @param {{ preventDefault: () => void; dataTransfer: { files: any; }; }} event
     */
    function handleDrop(event) {
        event.preventDefault();
        fileInput = event.dataTransfer.files;
    }

    //Handle file input
    /**
     * @param {{ target: { files: any; }; }} event
     */
    async function handleFileSelect(event) {
        const files = event.target.files;
        console.log(files);
        console.log(`File exists: ${files.length > 0}`);
        if (files.length > 0) {
            const file = files[0];
            console.log(`File name: ${file.name}`);
            console.log(`File type: ${file.type}`);
            console.log(`File size: ${file.size} bytes`);
            selectedFiles = [...selectedFiles, file];
            await handleImageUpload({ target: file });
        }
    }
    function handleClick() {
        // @ts-ignore
        fileInput.click();
    }

    /**
     * @param {{ target: { files: any[]; }; }} event
     */
    async function handleImageUpload(event) {
        // Check that the event target is an HTMLInputElement
        if (!(event.target instanceof HTMLInputElement)) {
            console.error("Event target is not an HTMLInputElement");
            return;
        }

        const file = event.target.files[0];
        const image = new Image();
        image.src = URL.createObjectURL(file);
        image.onload = async () => {
            const tensor = tf.browser.fromPixels(image).toFloat();
            const resized = tf.image.resizeBilinear(tensor, [224, 224]);
            const expanded = resized.expandDims();
            const model = await tf.loadLayersModel(
                "../../public/model/model.json"
            );
            const predictions = await model.predict(expanded).array();
            const healthyPrediction = predictions[0][0];
            const unhealthyPrediction = predictions[0][1];
            const threshold = 0.25;
            const difference =
                Math.abs(healthyPrediction - threshold) -
                Math.abs(unhealthyPrediction - threshold);
            if (difference > 0) {
                percentage = (healthyPrediction * 100).toFixed(2);
                name = "Healthy";
            } else {
                percentage = (unhealthyPrediction * 100).toFixed(2);
                name = "Unhealthy";
            }
            selectedFiles = [
                ...selectedFiles,
                ...Array.from(event.target.files),
            ];
        };
    }

    /* This is the reactive declaration for confidencePercent */
    $: if (percentage) {
        percentage = percentage;
    }
</script>

{#if typeof percentage !== "undefined"}
    <h2>AI thinks your teeth are {percentage}% healthy.</h2>
{:else}
    <h2>AI thinks you should upload an image.</h2>
{/if}

<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
<div
    class="files-drop"
    on:dragover={handleDragOver}
    on:drop={handleDrop}
    on:click={handleClick}
    tabindex="0"
    on:keydown={(event) => { if(event.key === "Enter") handleFileSelect } }
>
    Drag and drop your image here or click to add a file to add a file
    <input
        type="file"
        accept="image/*"
        style="display: none;"
        bind:this={fileInput}
        on:change={handleImageUpload}
    />
</div>


<style>
    @import url("https://fonts.googleapis.com/css2?family=Gloock&family=Open+Sans&family=Playfair+Display&family=Raleway&display=swap");
    :root {
        --nav-bar: #7d84b2;
        --nav-text: #d95d39;
        --primary: #8d98a7;
        --secondary: #dcccbb;
        --tertiary: #646e78;
    }

    h2 {
        font-family: "Gloock", serif;
    }
    .files-drop {
        max-width: 100%;
        height: 100px;
        background-color: var(--primary);
        opacity: 0.5;
        border-radius: 5px;
        display: flex;
        justify-content: center;
        padding: 10px;
        align-items: center;
        box-shadow: 0 20px 30px -14px rgba(0, 0, 0, 0.25);
    }
</style>
