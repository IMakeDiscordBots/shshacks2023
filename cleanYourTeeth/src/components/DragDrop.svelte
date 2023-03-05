<script>
    /**
     * @type {{ click: () => any; } | null}
     */
    export let fileInput = null;
    let imgThing;
    /**
     * @type {number}
     */
    let confidence;
    /**
     * @type {string}
     */
    let confidencePercent;
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
    function handleFileSelect(event) {
        const files = event.target.files;
        console.log(files);
        console.log(`File exists: ${files.length > 0}`);
        if (files.length > 0) {
            const file = files[0];
            console.log(`File name: ${file.name}`);
            console.log(`File type: ${file.type}`);
            console.log(`File size: ${file.size} bytes`);
        }
        selectedFiles = [...selectedFiles, ...files];
    }
    function handleClick() {
        // @ts-ignore
        fileInput.click();
    }

    /**
     * @param {{ key: string; }} event
     */
    function handleKeyDown(event) {
        if (event.key === "Enter") {
            handleClick();
        }
    }

    import * as tf from "@tensorflow/tfjs";

    async function handleImageUpload(event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = async () => {
            const image = new Image();
            image.src = reader.result;
            imgThing = image.src;
            image.onload = async () => {
                const tensor = tf.browser.fromPixels(image).toFloat();
                const resized = tf.image.resizeBilinear(tensor, [224, 224]);
                const expanded = resized.expandDims();
                const model = await tf.loadLayersModel(
                    "../../public/model/model.json"
                );
                const prediction = model.predict(expanded).dataSync();
                confidence = Math.max(...prediction);
                confidencePercent = (confidence * 100).toFixed(2);
                console.log(`The confidence rate is ${confidence}`);
            };
        };
        reader.readAsDataURL(file);
    }

    /* This is the reactive declaration for confidencePercent */
    $: if (confidence) {
        confidencePercent = (confidence * 100)?.toFixed(2);
    }
</script>

{#if typeof confidencePercent !== "undefined"}
    <h2>AI thinks your teeth are {confidencePercent}% healthy.</h2>
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
    on:keydown={handleKeyDown}
    on:change={handleImageUpload}
    on:change:{handleFileSelect}
>
    Drag and drop your image here or click to add a file to add a file
    <input
        type="file"
        accept="image/*"
        style="display: none;"
        bind:this={fileInput}
        on:change={handleFileSelect}
    />
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Gloock&family=Open+Sans&family=Playfair+Display&family=Raleway&display=swap');
    :root {
        --nav-bar: #7d84b2;
        --nav-text: #d95d39;
        --primary: #8d98a7;
        --secondary: #dcccbb;
        --tertiary: #646e78;
    }

    h2 {
        font-family: 'Gloock', serif;
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
