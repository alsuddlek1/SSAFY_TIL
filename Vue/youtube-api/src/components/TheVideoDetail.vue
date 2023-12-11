<template>
  <div>
    <!-- v-bind:attrs="JS expression" -->
    <iframe 
      :src="imgSrc" 
      frameborder="0"
    ></iframe>
    <p>{{ selectedVideo.snippet.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'TheVideoDetail',
  props: {
    selectedVideo: Object
  },
  computed: {
    imgSrc() {
      return `https://www.youtube.com/embed/${this.selectedVideo.id.videoId}`
    }
  }
}
</script>

<style>

</style>