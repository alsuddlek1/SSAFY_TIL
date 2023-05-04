import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  getters: {
    // 6.
    messageLength(state){
      return state.message.length
    },
    doubleLength(state, getters){
      return getters.messageLength * 2
    },
  },
  mutations: {
    // 5.
    CHANGE_MESSAGE(state, payload){
      state.message = payload
    }
  },
  actions: {
    // 4.
    changeMessage(context, message){
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
