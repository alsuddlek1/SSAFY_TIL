<template>
  <div @click="videoSelect">
    {{ video.snippet.title }}
  </div>
</template>

<script>
export default {
  name: 'TheVideoListItem',
  props: {
    video: Object
  },
  methods: {
    videoSelect() {
      this.$emit('video-select', this.video)
    }
  }
}
</script>

<style>

</style>