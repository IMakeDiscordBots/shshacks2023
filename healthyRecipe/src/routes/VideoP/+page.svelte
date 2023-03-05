<script>
  import Header from "../../components/header.svelte";
  import * as tmImage from "@teachablemachine/image";
  /**
   * @type {HTMLVideoElement | null}
   */
  let videoSource = null;
  let loading = false;

  /**
   * @type {any}
   */
  let errorMessage;
  /**
   * @type {tmImage.CustomMobileNet}
   */
  let model;

  let percentage = "";
  let name = "";

  const URL = "model";
  const modelURL = URL + "../../../public/model/model.json";
  const metadataURL = URL + "../../../public/model/metadata.json";
  const obtenerVideoCamara = async () => {
    try {
      loading = true;
      model = await tmImage.load(modelURL, metadataURL);

      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });

      // @ts-ignore
      videoSource.srcObject = stream;
      // @ts-ignore
      videoSource.play();

      loading = false;

      setInterval(predict, 1000);
    } catch (error) {
      console.log(error);
    }
  };

  async function predict() {
    const predictions = await model.predict(videoSource);
    const [chosenPrediction] = predictions.sort(
      (/** @type {any} */ a, /** @type {{ probability: any; }} */ b) =>
        b.probability
    );

    if (chosenPrediction) {
      percentage = (chosenPrediction.probability * 100).toFixed(2) + "%";
      // @ts-ignore
      name = classNameToLabel(chosenPrediction.className);
    }

    /**
     * @param {any} className
     */
    function classNameToLabel(className) {
      switch (className) {
        case "Healthy":
          return "Healthy";
        case "Unhealthy":
          return "Unhealthy";
      }
    }
  }
</script>
<Header />
<main>
  <h1>Teeth AI Model</h1>
  <!-- svelte-ignore a11y-media-has-caption -->
  <video bind:this={videoSource} />
  <button on:click={obtenerVideoCamara}>Analyze Your Teeth</button>
  {#if errorMessage}
    <h2>{errorMessage}</h2>
  {:else if loading}
    <h2>Loading ...</h2>
  {:else if percentage && name}
    <h2>AI {percentage} certain your teeth is {name}</h2>
  {/if}
</main>

<style>
  main {
    width: 100%;
    height: 100vh;
    padding: 0;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  video {
    display: block;
    margin: 20px auto;
  }

  h1,
  h2 {
    text-align: center;
  }

  h1 {
    font-size: 40px;
  }

  h2 {
    font-size: 20px;
  }

  .button {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #4CAF50;
  border: none;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  }
</style>
