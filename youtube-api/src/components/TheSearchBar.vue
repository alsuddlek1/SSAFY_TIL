<template>
  <div>
    <!-- root element는 오직 하나 -->
    <!-- enter 키가 입력되면 함수 실행 -->
    <input 
      type="text"
      @keydown.enter="onSearch"
    >
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods: {
    onSearch(event) {
      // App.vue 에게 enter키가 입력 되었음을 알리면서
      // input 태그의 value를 올려준다.
      this.$emit('on-search', event.target.value)
    }
  }
}
</script>

<style>

</style>