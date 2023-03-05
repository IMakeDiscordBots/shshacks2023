<script>
    import Header from "../../components/header.svelte";
</script>

<Header />

<body>
    <body>
        <div class="main">
            <div class="content">
                <h1>About</h1>
                <div class = "about">
                    <p >
                        Dental health is a critical aspect of overall health and well-being. Neglecting dental health can lead to a host of negative consequences, including tooth decay, gum disease, and even systemic health problems such as heart disease and stroke. Conversely, good dental health has numerous benefits that impact physical, social, and psychological well-being.
                    </p>
                    <p >
                        When individuals prioritize their dental health by maintaining good oral hygiene practices such as brushing and flossing regularly, eating a healthy diet, and visiting the dentist for routine checkups and cleanings, they can prevent dental problems that can cause pain, discomfort, and difficulty in eating and speaking. Neglecting dental health can lead to malnutrition, social isolation, depression, and other mental health problems.
                    </p>
                    <p >
                        For children, dental health is especially important as it can affect their growth and development. Neglecting dental health in children can cause pain and discomfort, leading to difficulty in eating, speaking, and sleeping, which can affect their ability to learn and perform well in school. Additionally, dental problems in children can impact the development of their permanent teeth, leading to long-term dental problems.
                    </p>
                    <p >
                        Individuals who maintain good dental health can improve their physical health, appearance, self-confidence, and social interactions, while preventing serious health problems. Therefore, it is essential to establish good oral hygiene practices early on, as well as to regularly visit the dentist for checkups and cleanings.
                    </p>
                </div>
            </div>
        </div>
    </body>
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
