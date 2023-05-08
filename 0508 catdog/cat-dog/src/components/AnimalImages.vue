<template>
  <div>
    <!-- select의 값이 바뀔 때 마다 state.status를 바꾼다 -> ~하면 ~한다. -->
    <select 
      @change="onChange"
      name="status" 
      id="setStatus">
        <!-- 사용자에게 보여질 텍스트와 실제 사용될 value 구분 잘하기 -->
        <option value="all">전체</option>
        <option value="cat">애옹</option>
        <option value="dog">댕댕</option>
    </select>
    <ul class="card-list">
      <!-- 모든 state.images 가져와서 반복 -->
      <AnimalCard 
        v-for="image in images"
        :key="image.id"
        :image="image"
      />
    </ul>
  </div>
</template>

<script>
// import { mapgetters}
import AnimalCard from './AnimalCard.vue'

export default {
  name : 'AnimaImages',
  components : {
    AnimalCard,
  },
  methods: {
    onChange(event){
      this.$store.dispatch('changeStatus', event.target.value)
    }
  },
  computed: {
    // 종속대상의 값이 변경될때 새롭게 값을 계산하고, 그 결과인 함수의 반환값을 사용할 수 있게됨
    images(){
      return this.$store.getters.getStatusByImages
    }
  }
}
</script>

<style>
.card-list{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>