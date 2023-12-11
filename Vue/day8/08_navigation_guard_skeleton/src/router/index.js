import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView'
import DogView from '@/views/DogView'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    ///// 라우터 가드 /////
    beforeEnter(to, from, next) {
      if (isLoggedIn === true){
        console.log('이미 로그인함')
        next({name: 'home'})
      } else { // 로그인이 되어있지 않다면 로그인 페이지로 이동
        next()
      }
    }
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  {
    path: '*', // 위에 모두 해당하지 않는 모든 것 죽, 맨 아래에 위치해야함
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router/index.js

////// 전역 가드 /////////
// router.beforeEach((to, from, next) => {
//   // 로그인 여부 판별
//   const isLoggedIn = true // 로그인 됨(false 일때 로그인 안됨)
//   // 로그인이 필요한 페이지 지정
//   const authPages = ['hello']
//   // 로그인이 필요 없는 페이지 지정
//   // const allowAupages = ['login'] 
//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   const isAuthRequired = authPages.includes(to.name)
//   // const isAuthRequired = !allowAupages.includes(to.name) //로그인이 필요없는 페이지 지정했을때
  
//   if (isAuthRequired && !isLoggedIn){
//     console.log('login으로 이동')
//     next({name: 'login'}) // login 페이지로 이동하므로, login페이지 + to로 이동 로 이동 두번 뜸
//   } else {
//     console.log('to로 이동')
//     next()
//   }
// })
export default router
