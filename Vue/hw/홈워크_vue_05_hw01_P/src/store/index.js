import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter : 0
  },
  getters: {
    counterDoble(state){
      return state.counter
    }
  },
  mutations: {
    
  },
  actions: {
    increase(context, counter){
      context.commit('UPNUMBER', counter)
    }
  },
  modules: {
  }
})
