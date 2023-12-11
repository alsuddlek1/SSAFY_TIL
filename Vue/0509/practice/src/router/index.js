import Vue from 'vue'
import VueRouter from 'vue-router'
import FirstView from '../views/FirstView.vue'
// import SecondView from '../views/SecondView.vue'
import TheLunchView from '../views/TheLunchView.vue'
import TheLottoView from '../views/TheLottoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'first',
    component: FirstView
  },
  {
    path: '/second/:valueName',
    name: 'second',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/SecondView.vue')
    // component: SecondView
  },
  { // 경로
    path: '/lunch',
    name: 'lunch',
    component: TheLunchView
  },
  {
    path: '/lotto/:lottoNum',
    name: 'lotto',
    component : TheLottoView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
