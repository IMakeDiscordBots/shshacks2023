<header>
    <nav class = "navbar">
        <ul class = "nav-items">
            <li class = "nav-item"><a href = "/">Home</a></li>
            <li class = "nav-item"><a href = "/info">About</a></li>
            <li class = "nav-item"><a href = "/FAQs">FAQs</a></li>
            <li class = "nav-item"><a href = "/VideoP">Video</a></li>
            <li class = "nav-item"><a href = "/Contact">Contact Us</a></li>
        </ul>
    </nav>
</header>

<style>
    :root {
        --nav-bar: #7D84B2;
        --nav-text: #D95D39;
        --primary: #8D98A7;
        --secondary: #DCCCBB;
        --tertiary: #646E78;
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
</style>