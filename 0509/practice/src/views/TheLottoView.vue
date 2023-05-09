<template>
  <div>
    <h1>lotto</h1>
    <button @click="onClick">getLottoNym</button>
    <!-- <p>{{lottoNums}}</p> -->
    <LottoItem 
    :lotto-nums="lottoNumList"/>
  </div>
</template>

<script> 
import _ from 'lodash'
import LottoItem from '../components/LottoItem.vue'

export default {
  name: 'TheLottoView',
  data(){
    return{
      lottoNumList : [],
      lottoNums: [],
    }
  },
  methods: {
    onClick(){
      const params = this.$route.params.lottoNum
      for (let i=0; i<params; i++){
        const numbers = _.range(1, 46)
        const lottoNumbers = _.sampleSize(numbers, 6)
        this.lottoNums = _.sortBy(lottoNumbers)
        this.lottoNumList.push(this.lottoNums)
      }
    }
  },
  components: {
    LottoItem
  }
}
</script>

<style>

</style>