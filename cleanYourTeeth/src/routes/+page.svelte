<script>
    import Header from "../components/header.svelte";
    import DragDrop from "../components/DragDrop.svelte";
</script>

<Header />

<body>
    <div class="main">
        <div class="content">
            <h1>clean your teeth.</h1>
            <p class = "about">
                <u>invest</u> in your <u>smile</u>, it's the <u>best</u> accessory you'll ever wear.
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
        background: repeating-linear-gradient(-45deg, #B1D9CA, #B1D9CA 50px, #E5FDF4 50px, #E5FDF4 100px);
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
