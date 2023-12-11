<template>
  <div>
    <h1>로또 페이지</h1>
    <button @click="onClick">getLottoNum</button>
    <p>{{ lottoNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLottoView',
  data() {
    return { 
      lottoNums: []
    }
  },
  methods: {
    onClick() {
      // variable routing에 (사용자가 입력하거나 넘겨준 params에 들어 있는 데이터는?)
      const params = this.$route.params.lottoNum

      // 1부터 45까지의 숫자로 이루어진 배열 만들기
      const numbers = _.range(1, 46)
      // 1부터 45까지의 숫자 중 비복원추출 6개 하기
      const lottoNumbers = _.sampleSize(numbers, params)
      // 추출된 숫자 정렬하기
      this.lottoNums = _.sortBy(lottoNumbers)
    }
  }
}
</script>

<style>

</style>