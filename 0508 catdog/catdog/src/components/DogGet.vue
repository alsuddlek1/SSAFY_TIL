<template>
  <div>
    <button @click="getdog">dog</button>
    <img :src="dogurl" height="300px" width="300px">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'DogGet',
  computed: {
    dogurl(){
      return this.$store.state.dogurl
    }
  },
  methods: {
    getdog(){
      axios({
        method : 'get',
        url : 'https://dog.ceo/api/breeds/image/random',
      })
      .then(res => {
        // res.data.message
        this.$store.dispatch('getdog', res.data.message)
      })
    }
  }
}
</script>

<style>

</style>