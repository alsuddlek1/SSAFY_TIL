<template>
  <div id="app">
    <h1>나의 첫번째 유튜브 프로젝트</h1>
    <!-- 3. 검색 바 컴포넌트 보여준다 -->
    <TheSearchBar
      @on-search="youtubeSearch"
    />
    <!-- selectedVideo가 없으면 렌더링이 안되게 한다. -->
    <TheVideoDetail
      v-if="selectedVideo"
      :selected-video="selectedVideo"
    />
    <TheVideoList
      :video-list="videoList"
      @video-select="videoSelect"
    />
    
  </div>
</template>

<script>
// 1. 불러온다.
import TheSearchBar from './components/TheSearchBar.vue'
import TheVideoList from './components/TheVideoList.vue'
import TheVideoDetail from './components/TheVideoDetail.vue'
import axios from 'axios'

export default {
  name: 'App',
  // 2. 등록한다.
  components: {
    TheSearchBar,
    TheVideoList,
    TheVideoDetail
  },
  data() {
    return {
      videoList: [],
      selectedVideo: null
    }
  },
  methods: {
    youtubeSearch(keyWord) {
      const params = {
        type: 'video',
        q: keyWord,
        key: '123',
        part: 'snippet',
      }
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params
      })
        .then(res => {
          this.videoList = res.data.items
        })
        .catch(err => console.log(err))

    },
    videoSelect(selectedVideo) {
      this.selectedVideo = selectedVideo
    }
  }
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
