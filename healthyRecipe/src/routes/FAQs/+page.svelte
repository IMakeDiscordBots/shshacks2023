<script>
    import Header from "../../components/header.svelte"
</script>

<Header />

<body>
    <div class="main">
        <div class="content">
            <h1>FAQs</h1>
            <div class = "about">
                <p>
                    Q: What steps does this website take to protect my privacy?
                </p>
                <p>
                    A: At this website, respecting your privacy is of the utmost importance. To ensure the safety of your personal information, we take several measures. First and foremost, we use secure connections and encryption protocols to safeguard the data that you transmit to our site. We also adhere to strict data protection policies and maintain a secure server infrastructure. Additionally, we ensure that the images you upload are completely deleted from our servers immediately after usage, ensuring that your personal data does not get leaked to third-party sources. At this website, we are committed to protecting your privacy and ensuring a safe and secure online experience.
                </p>
                <p>
                    Q: How do I know this information is factual?
                </p>
                <p>
                    A: Our website uses machine learning AI technology to compare teeth health based on objective and verifiable data points. We collect data from reputable sources and analyze it using advanced algorithms to provide accurate and reliable information. Our AI models are trained on large datasets of dental health information, ensuring that the results are statistically significant and based on sound scientific principles. In addition, we constantly update and improve our algorithms to ensure that the information we provide is up-to-date and accurate. Ultimately, our goal is to provide you with the most reliable and trustworthy information possible to help you maintain optimal dental health.
                </p>
                <p>
                    Q: How does our grading scale work?
                </p>
                <p>
                    A: Our website evaluates dental health using a grading scale of 1-4, where 1 represents optimal teeth health and 4 represents poor teeth health. The grading system is based on objective and verifiable data points, such as the presence of cavities, gum disease, and other dental conditions. Our AI algorithm analyzes the data and assigns a grade based on the severity of the condition and its impact on dental health. The grading scale is designed to provide a clear and easy-to-understand assessment of dental health, helping users to identify areas of concern and take steps to improve their oral health.
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
