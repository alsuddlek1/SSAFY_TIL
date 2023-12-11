<template>
  <div id="app">
    
    
    <CatGet/>
    <DogGet/>
  </div>
</template>


<script>
import CatGet from './components/CatGet.vue'
import DogGet from './components/DogGet.vue'

export default {
  name: 'App',
  components: {
    CatGet,
    DogGet,
  },
  computed : {
  },
  methods : {
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
