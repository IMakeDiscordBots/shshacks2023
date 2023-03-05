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

<header>
    <nav class = "navbar">
        <ul class = "nav-items">
            <li class = "nav-item"><a href = "#">Home</a></li>
            <li class = "nav-item"><a href = "#">Info</a></li>
            <li class = "nav-item"><a href = "#">How?</a></li>
        </ul>
    </nav>
</header>
<body>
    <div class="main">
        <div class="content">
            <h1>clean your teeth.</h1>
            <p class = "about">
                test TEST
            </p>
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
        </div>
    </div>
</body>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Gloock&family=Open+Sans&family=Playfair+Display&family=Raleway&display=swap');
    :root {
        --nav-bar: #7D84B2;
        --nav-text: #D95D39;
        --primary: #8D98A7;
        --secondary: #DCCCBB;
        --tertiary: #646E78;
    }
    body {
        display: flex;
        justify-content: center;
        margin: auto;
        padding: 40px;
        background-color: #D5F9DE;
    }
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        box-shadow: 0 20px 30px -14px rgba(0, 0, 0, 0.25);
        background: #EADEDA;
        height: 40px;
    }
    nav ul {
        list-style: none;
        display: flex;
        gap: 20px;
        margin: 0;
    }
    nav a {
        color: var(--nav-bar);
        text-decoration: none;
        padding: 5px 10px;
        border-radius: 5px;
        transition: color 0.3s ease;
        font-size: 20px;
        font-family: 'Gloock', serif;
    }
    nav a:hover {
        color: #333;
    }
    .content {
        margin: auto;
        border-radius: 10px;
        background-color: #FAF9F6;
        padding: 40px;
        box-shadow: 0 20px 30px -14px rgba(0, 0, 0, 0.25);
    }
    h1 {
        font-family: 'Gloock', serif;
    }
    .about {
        font-family: 'Raleway', sans-serif;
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
