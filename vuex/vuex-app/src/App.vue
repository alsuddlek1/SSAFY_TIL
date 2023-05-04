<template>
  <div id="app">
    <h1> {{ message }}의 길이 {{ messageLength}}</h1>
    <h2> x2 : {{ doubleLength }}</h2>
    <!-- 1.. inputdata에 text를 입력하고 엔터를 누르면 changeMessage라는 메서드 실행 -->
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return {
      inputData: null,
    }
  },
  methods: {
    // 3.. changeMessage는 newMessage를 담아서 dispath.changeMessage를실행
    changeMessage(){
      const newMessage = this.inputData
      // dispath는 store에서 실행 (dispath(action이름))
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    }
  },
  components:{

  },
  computed: {
    // 2.
    message(){
      return this.$store.state.message
    },
    messageLength(){
      return this.$store.getters.messageLength
    },
    doubleLength(){
      return this.$store.getters.doubleLength
    }
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
