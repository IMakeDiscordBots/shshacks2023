<script>

    // Later, perhaps in a form 'submit' handler or the input's 'change' handler:

    /**
     * @type {{ click: () => any; } | null}
     */
    export let fileInput = null;
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

        fetch('http://localhost:3000/', {
            mode: 'no-cors',
            method: 'POST',
            body: "hello there",
        })
        .then((response) => console.log(response))
        .then((data) => console.log(data))
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
</script>

<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
<div
    class="files-drop"
    on:dragover={handleDragOver}
    on:drop={handleDrop}
    on:click={handleClick}
    tabindex="0"
    on:keydown={handleKeyDown}
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
    :root {
        --nav-bar: #7d84b2;
        --nav-text: #d95d39;
        --primary: #8d98a7;
        --secondary: #dcccbb;
        --tertiary: #646e78;
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
