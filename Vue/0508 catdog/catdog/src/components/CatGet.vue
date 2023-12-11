<template>
  <div>
    <button @click="getcat">cat</button>
    <img :src="caturl" height="300px" width="300px">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'CatGet',
  computed: {
    caturl(){
      return this.$store.state.caturl
    },
  },
  methods : {
    getcat(){
      axios({
        method : 'get',
        url : 'https://api.thecatapi.com/v1/images/search',
      })
      .then(res => {
        // this.$store.state.caturl = res.data[0].url
        this.$store.dispatch('getcat',res.data[0].url )
      })
    },
  }
}
</script>

<style>

</style>