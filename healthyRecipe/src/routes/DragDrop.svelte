<script>
    export let file = null;
    
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
        file = event.dataTransfer.files;
        console.log(file);
        console.log(`File exists: ${typeof(file) !== "undefined"}`)
    }
    /**
     * @param {{ target: { files: any; }; }} event
     */
    function handleFileSelect(event) {
        const files = event.target.files;
    }
</script>

<div class = "files-drop" on:dragover = {handleDragOver} on:drop = {handleDrop} onclick = {() => fileInput.click()}>
    Drag and drop your image here or click to add a file to add a file
    <input
        type = "file"
        accept="image/*"
        style="display: none;"
        bind:this = {file}
        on:change = {handleFileSelect}
    />
</div>

<style>
    :root {
        --nav-bar: #7D84B2;
        --nav-text: #D95D39;
        --primary: #8D98A7;
        --secondary: #DCCCBB;
        --tertiary: #646E78;
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