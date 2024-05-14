<template>
  <div>
    <div class="container">
      <div>
        <h1>lé péi d'y mon2</h1>
      </div>
      <div class="container">
        <button @click="toggleDarkMode">
          <img src="./images/lune.png" alt="lune" class="dark">
        </button>
      </div>
    </div>
    <hr>
    <div v-for="country in countries" :key="country.name.common" class="country">
      <h2>{{ country.name.common }}</h2>
      <img :src="country.flags.png" :alt="'Drapeau de ' + country.name.common">
      <p>Région: {{ country.region }}</p>
      <p>Population: {{ country.population }}</p>
      <p>Capitale: {{ country.capital[0] }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      countries: []
    };
  },
  mounted() {
    fetch("https://www.restcountries.com/v3.1/areponsell").then(reponse =>
    {
      return reponse.json();
    }).then(data =>{
      this.countries = data;
      this.countries_show = data;
      this.region.push("Monde");
      this.countries.forEach(element => {
        if(!this.region.includes(element.region)){
          this.region.push(element.region)
        }
      })
    })
    //this.getCountryData();
    }
}
  /*
  methods: {
    async getCountryData() {
      try {
        const response = await fetch("https://www.restcountries.com/v3.1/all");
        const countriesData = await response.json();
        this.countries = countriesData.map(element => {
          return {
            name: element.name.common,
            population: element.population,
            capital: element.capital[0],
            region: element.region,
            flag: element.flags.svg
          };
        });
      } catch (error) {
        console.error('Error fetching country data:', error);
      }
    }, 
    toggleDarkMode() {
      
      console.log("Toggle Dark Mode");
    }
  }
};
*/
</script>

<style>
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  --dark: #021e5b;
  --back: rgb(232, 232, 220);
  --font-color: rgb(18, 18, 18);
  background-color: var(--back);
  color: var(--font-color);

  width: 5% 95%;
  height: 5% 95%;
  justify-content: center;
  align-items: center;
}

hr {
  border-top: var(--dark) 2px;
  margin: 20px 0;
}

h1 {
  line-height: 2;
  font-weight: 600;
}

.container {
  display: flex;
  justify-content: space-between;
  text-align: center;
  margin-left: 10px;
  margin-right: 10px;
}

.dark {  
  background-color: var(--back);
  display: flex;
  max-width: 40px;
  max-height: 40px;
}

.dark img {
  width: 2%;
  border: none;
  max-width: 50px;
  max-height: 50px;
  margin-right: 500px;

  border-radius: 2px;
}

button:hover {
  cursor: pointer;
  background-color: var(--dark);
  color: white;
  transition: width 0.5s ease, height 0.5s ease, background-color 0.5s ease;
}

.country {
  display: flex;
  background-color: var(--back);
  border: 5px black;
}

.country:hover{
  background-color: #021e5b;
  color: white;
  transition: width 0.5s ease, height 0.5s ease, background-color 0.5s ease;
}
</style>