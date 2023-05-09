<template>
  <div>
    <h1>오늘 대웅이의 저녁 메뉴</h1>
    <button @click="onClick">pick lunch</button>
    <p>{{menu}}</p>
    <input type="text" v-model="nums">
    <button @click="goLottoOnClick">golotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunchView',
  data(){
    return{
      menu : null,
      lunchMenu: ['안성탕면', '짜파게티', '신라면', '라면 먹지마', '왕뚜껑' ],
      nums : null,
    }
  },
  methods: {
    onClick(){
      this.menu = _.sample(this.lunchMenu) // 무작위 값
    } ,
    goLottoOnClick(){
      // lotto 페이지가 렌더링 되도록 router 이동
      // lottoNum에 데이터 담아서
      if (this.nums){
        this.$router.push({name:'lotto', params: {lottoNum:this.nums}})
        } else {
          alert ('로또 숫자 입력부탁')
        }

      // 게시글 생성 버튼이 눌렸을 때 실행 될 메서드
        // vuex를 쓰고 있었다면 게시글 생성 actions 호출
      //serve에 게시글 생성 해달라는 post 요청을 axios 보낸다.
        // serve가 게시글 생성후, 생성된 게시글의 정보 (pk등) json 형태로 응답 한다.
        // 요청 성공 했으니 response.data.pk --> 방금 생성된 게시글의 pk 정보
        // 사용자에게 그 게시글의 '/detail/:article_pk' 경로로 이동하도록 $router.push

      // detail component에서는 무슨일이?
        // route.params.article_pk 에는 특정 게시글의 pk 값이 들어 있다.
        // 그 pk 값으로 serve GET 요청 보낸다.
        // 게시글의 상세정보를 서버로부터 받아와서 화면에 그린다.
    }
  }
}
</script>

<style>

</style>