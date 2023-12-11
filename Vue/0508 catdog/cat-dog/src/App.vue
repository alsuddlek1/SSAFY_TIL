<template>
  <div id="app">
    <!-- 클릭했을때 AJAX 요청을 보내도록 해야한다. -->
    <!-- ~~하면, ~~ 한다 : event에 대한 일 처리 -->
    <!-- 1. @click -> method 실행(vue instance의 method를 호출) -->
    <button @click="getCatImage">getCat</button>
    <!-- 9. store의 -->
    <button @click="getDogImage">getDog</button>
    <hr>
    <AnimalImages />
  </div>
</template>

<script>
// 7?8.
import { mapActions } from 'vuex'
import AnimalImages from './components/AnimalImages.vue'

// 현재 컴포넌트의 Vue Instance의 method를 실행 -> method들을 정의하고, 대상을 호출
export default {
  // 6.
  state : {
    images: []
  },
  name: 'App',
  components: {
    AnimalImages,
  },
  methods: {
    // 배열형태지만, 객체형태로도 가능
    // 한번이 아닌 여러번 사용 가능 
    ...mapActions(['getDogImage']),
    // 각각의 actions의 method 각각 다르게 호출해서 custom 가능

    // 2.
    getCatImage(){
      // actions에서 axios 요청을 보낼 method 정의 후 다시 돌아오기
      // 4. actions에 정의한 getCatImage를 호출 (payload 따로 없음)
      this.$store.dispatch('getCatImage')
    },
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
