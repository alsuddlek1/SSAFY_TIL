import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    caturl : '',
    dogurl : ''
  },
  getters: {
  },
  mutations: {
    GET_CAT(state, url){
      state.caturl = url
    },
    GET_DOG(state, url){
      state.dogurl = url
    }
  },
  actions: {
    getcat(context, url){
      context.commit('GET_CAT', url)
    },
    getdog(context, url){
      context.commit('GET_DOG', url)
    }
  },
  modules: {
  }
})
