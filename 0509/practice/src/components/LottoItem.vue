<template>
  <div>
    <p v-for="(lottoNum, lotto) in lottoNums" :key="lotto">{{lottoNum}}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name : 'LottoItem',
  props: {
    lottoNums: Array,
  },
  filters: {
    sortArray(lottoNums){
      return _.sortBy(lottoNums)
    },
    joinArray(lottoNums){
      return lottoNums.join(' ')
    }
  }
}
</script>

<style>

</style>