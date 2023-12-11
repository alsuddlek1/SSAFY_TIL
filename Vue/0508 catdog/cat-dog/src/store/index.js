import Vue from 'vue'
import Vuex from 'vuex'

const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'
const DOG_API_URL = 'https://dog.ceo/api/breeds/image/random'

Vue.use(Vuex)
import axios from 'axios'

export default new Vuex.Store({
  state: {
    images:[],
    // 사용자가 select를 바꿀때마다 바뀌어야 함
    status: 'all',
  },
  // comoputed랑 같은 역할
  getters: {
    getStatusByImages(state){
      // 사용자가 선택한 status에 따라서 반환해줄 배열의 내용물을 바꾼다.
      const images = state.images.filter(image => {
        // cat 이면 고양이
        if (state.status === 'dog'){
          return image.status === 'dog'
        } else if (state.status === 'cat'){
          // dog 이면 강아지
          return image.status === 'cat'
        }
        // all 이면 모든 이미지
        return image
      })
      return images
    }
  },
  // 6.
  mutations: {
    // 상태 변화
    GET_IMAGE(state, payload){
      state.images.push(payload)
    },
    CHANGE_STATUS(state, payload){
      state.status = payload
    }
  },
  actions: {
    // 3. actions에 정의하는 메서드는 인자로 context를 첫번째로 넘겨받음
    // context를 통해서 다른 객체나 속성에 접근할 일 없이 commit (mutations를 호출만 할거라면)
    // const commit = context.commit
    // const {commit} = context
    getCatImage({commit}){
      axios({
        method: 'get',
        url : CAT_API_URL
      })
      .then(res => {
        // state에 저장될 데이터 전처리
        // 5.
        const payload = {
          id : new Date().getTime(),
          url : res.data[0].url,
          status : 'cat'
        }
        commit('GET_IMAGE', payload)
        // 3.
        // console.log(res)
        res.data[0].url
      })
      .catch(err => console.log(err))
    },
    getDogImage({commit}){
      axios({
        method: 'get',
        url : DOG_API_URL
      })
      .then(res => {
        const payload = {
          id : new Date().getTime(),
          url : res.data.message,
          status : 'dog'
        }
        commit('GET_IMAGE', payload)
      })
      .catch(err => console.log(err))
    },
    changeStatus({ commit }, payload){
      commit('CHANGE_STATUS', payload)
    }
  },
  modules: {
  },
  // plugins : {
  //   createPersistedState()
  // }
})
