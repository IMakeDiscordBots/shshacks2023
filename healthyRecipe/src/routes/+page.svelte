<script>
    import Header from "../components/header.svelte";
    import DragDrop from "../components/DragDrop.svelte"
</script>

<Header />

<body>
    <div class="main">
        <div class="content">
            <h1>clean your teeth.</h1>
            <p class = "about">
                invest in your smile, it's the best accessory you'll ever wear.
            </p>
            <DragDrop />
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
        padding: 120px;
        background-color: #D5F9DE;
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
</style>
