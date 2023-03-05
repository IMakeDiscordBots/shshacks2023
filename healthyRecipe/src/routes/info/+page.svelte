<script>
    import Header from "c:/Users/21Jon/OneDrive/Documents/GitHub/shshacks2023/healthyRecipe/src/components/header.svelte"
</script>

<Header />

<body>
    <div class="main">
        <div class="content">
            <h1>About</h1>
            <div class = "about">
                <p >
                    Dental health is a critical component of overall health and well-being. It involves maintaining good oral hygiene practices, such as brushing and flossing regularly, eating a healthy diet, and visiting the dentist for routine checkups and cleanings. Good dental health has numerous benefits that impact physical, social, and psychological well-being.
                </p>
                <p >
                    One of the most important reasons to prioritize dental health is the link between oral health and systemic health. Poor dental health has been linked to a range of serious health problems, including heart disease, stroke, diabetes, respiratory infections, and dementia. When oral bacteria enter the bloodstream, they can cause inflammation and damage to other parts of the body, leading to these health problems. By maintaining good oral hygiene practices and visiting the dentist regularly, individuals can reduce their risk of developing these serious health problems.
                </p>
                <p >
                    Another benefit of good dental health is improved overall physical health. Dental problems, such as cavities and gum disease, can cause pain, discomfort, and difficulty in eating and speaking. This can lead to malnutrition and other health problems. By preventing dental problems through good oral hygiene practices and regular dental checkups, individuals can ensure that their teeth and gums are healthy, allowing them to eat and speak comfortably and stay healthy.
                </p>
                <p >
                    In addition to its impact on physical health, dental health also has social and psychological benefits. Poor dental health can cause bad breath, discolored or missing teeth, and other cosmetic issues that can affect one's confidence and self-esteem. This can lead to social isolation, depression, and other mental health problems. On the other hand, good dental health can improve one's appearance, boost self-confidence, and enhance social interactions.
                </p>
                <p >
                    For children, dental health is especially important, as it can affect their growth and development. Poor dental health in children can cause pain and discomfort, leading to difficulty in eating, speaking, and sleeping. This can affect their ability to learn and perform well in school. In addition, dental problems in children can affect the development of their permanent teeth, leading to long-term dental problems.
                </p>
                <p >
                    To ensure good dental health in children, parents should establish good oral hygiene practices early on. This includes cleaning their children's teeth as soon as they appear, using a soft-bristled toothbrush and water. As the child grows older, they can start using fluoride toothpaste and flossing regularly. Regular dental checkups and cleanings can also help prevent dental problems and ensure that any problems are detected and treated early on.
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
