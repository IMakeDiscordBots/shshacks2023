<script>
    export let header = "null";
    export let body = "undefined";
</script>

<body>
    <div class="main">
        <div class="content">
            <h1>{header}</h1>
            <div class = "about">
                <p >
                  {body}  
                </p>
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
        padding: 100px;
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