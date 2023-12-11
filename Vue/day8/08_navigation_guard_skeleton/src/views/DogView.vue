<template>
  <div>
    <p v-if="!imgSrc">{{message}}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data(){
    return {
      imgSrc: null,
      message: '로딩중 ,,, '
    }
  },
  methods: {
    getDogImage(){
      const breed = this.$route.params.breed
      const dogImageSerachURL = `https://dog.ceo/api/breed/${breed}/images/random`
      axios({
        method: 'get',
        url: dogImageSerachURL
      })
      .then((response) => {
        console.log(response)
        const dogimgSrc = response.data.message
        this.imgSrc = dogimgSrc
      })
      .catch((error) => {
        console.log(error)
        this.message = `${this.$route.params.breed}는 없는 품종이에야`
      })
    }
  },
  created(){
    this.getDogImage()
  }
}
</script>

<style>

</style>