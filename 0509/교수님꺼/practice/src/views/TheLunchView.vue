<template>
  <div>
    <h1>점심 메뉴 추천</h1>
    <button @click="onClick">pickLunch</button>
    <p>{{ menu }}</p>
    <input type="number" id="buyCount" @keydown.enter='goLottoOnBuy' v-model="count">
    <button @click="goLottoOnClick">go Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunchView',
  data() {
    return { 
      menu: null,
      lunchMenu: ['비냉', '소고기뭇국', '너구리', '고추잡채밥']
    }
  },
  created(){
    this.buyLotto()
  },
  methods: {
    

    goLottoOnClick() {
      // lotto 페이지가 렌더링 되도록 router 이동
      // lottoNum에 데이터 담아서
      this.$router.push({name:'lotto', params: {lottoNum: 6}})

      // 게시글 생성 버튼이 눌렸을때 실행 될 메서드
        // vuex를 쓰고 있었다면 게시글 생성 actions 호출
      // server에 게시글 생성 해달라는 post 요청을 axios로 보낸다.
        // server가 게시글 생성후, 생성된 게시글의 정보 (pk 등) json 형태로 응답 한다.
        // 요청 성공 했으니 then 메서드에서 response형태의 데이터를 받는다.
        // 그렇게 응답 받은 response.data.pk -> 방금 생성된 게시글의 pk 정보
        // 사용자에게 그 게시글의 `/detail/:article_pk` 경로로 이동하도록 $router.push

      // detail component에서는 무슨일이?
        // route.params.article_pk 에는 특정 게시글의 pk값이 들어있다.
        // 그 pk 값으로 server GET 요청 보낸다.
        // 게시글의 상세정보를 서버로부터 받아와서 화면에 그린다.
    }
  }

}
</script>

<style>

</style>