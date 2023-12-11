<template>
  <div>
    <!-- 부모로 넘겨받은 videoList 배열의 원소 하나하나를 -->
    <!-- 반복문 돌려서 그 객체 하나 video하나를 prop -->
    <TheVideoListItem
      v-for="video in videoList"
      :key="video.id.videoId"
      :video="video"
      @video-select="videoSelect"
    />
  </div>
</template>

<script>
import TheVideoListItem from './TheVideoListItem.vue'

export default {
  name: 'TheVideoList',
  components: {
    TheVideoListItem
  },
  // 부모로부터 넘겨 받은 데이터는
  // 내가 값을 바꿀수는 없지만
  // data에 정의한것과 똑같이 쓸 수 있다.
  props: {
    videoList: Array
  },
  methods: {
    videoSelect(selectedVideo) {
      this.$emit('video-select', selectedVideo)

    }
  }
}
</script>

<style>

</style>