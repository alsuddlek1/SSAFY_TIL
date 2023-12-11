<template>
  <div id="app">
    <h1>길이 {{ messageLength }}의 메시지 {{ msg }}를 입력받음</h1>
    <h3>x2 : {{ doubleLength }}</h3>
    <input type="text" @keyup.enter="onSubmit" v-model="inputData">
    <h1>{{level}}</h1>
    <button @click="uplevel">levelup</button>
  </div>
</template>

<script>
// 1.
import {mapState, mapActions, mapGetters} from 'vuex'

export default {
  name: 'App',
  components: {
  },
  // 1.
  created(){
    // this.$store.dispatch('localMessage')
    console.log(this.$store)
  },
  computed: {
    // message() {
    //   return this.$store.state.message
    // },
    // 얘랑 밑에 애랑, 밑에밑에 애랑 다 같음
    // 2.
    ...mapState(['age']),
    // 다른이름으로 쓰고싶을때 밑에꺼 씀
    ...mapState({
      msg: stage => stage.message,
      level: state => state.myModule.level
    }),
    // messageLength() {
    //     return this.$store.getters.messageLength
    // },
    // doubleLength() {
    //     return this.$store.getters.doubleLength
    // },
    ...mapGetters(['messageLength', 'doubleLength'])
  },
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    // changeMessage() {
    //   const newMessage = this.inputData
    //   this.$store.dispatch('changeMessage', newMessage)
    //   this.inputData = null
    // },
    // ...mapActions(['changeMessage'])
    ...mapActions({
      actionsChangeMessage: 'changeMessage',
      uplevel: 'incrementLevel'
    }),
    onSubmit(){
      const newMessage = this.inputData
      this.actionsChangeMessage(newMessage)
      this.inputData = null
    },
    // uplevel(){
    //   this.$store.dispatch('incrementLevel')
    // }
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
