<script>
    export let file = null;
    
    /**
     * @param {{ preventDefault: () => void; }} event
     */
    function handleDragOver(event) {
        event.preventDefault();
    }
    function handleDrop(event) {
        event.preventDefault();
        file = event.dataTransfer.files;
        console.log(file);
        console.log(`File exists: ${typeof(file) !== "undefined"}`)
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
            <div class = "files-drop" on:dragover = {handleDragOver} on:drop = {handleDrop}></div>
        </div>
    </div>
</body>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Gloock&family=Open+Sans&family=Playfair+Display&family=Raleway&display=swap');
    :root {
        --nav-bar: #0E1428;
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
    }
    header {
        background-color: var(--nav-bar);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
    }
    nav ul {
        list-style: none;
        display: flex;
        gap: 20px;
        margin: 0;
    }
    nav a {
        color: var(--nav-text);
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
        background-color: var(--secondary);
        padding: 40px;
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
        background-color: var(--tertiary);
        border-radius: 5px;
    }
</style>
