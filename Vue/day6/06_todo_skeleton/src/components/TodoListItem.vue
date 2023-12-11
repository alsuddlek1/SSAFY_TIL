<template>
  <div>
    <!-- 5. -->
    <li @click="updateTodo" :class="{ 'is-completed' : todo.isCompleted }">{{ todo.title }}</li>
    <!-- 1. delete 버튼 생성 -->
    <button @click="deleteTodo">DELETE</button>
  </div>
  
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  // 2. deleteTOdo액션 실행하고 todo를 인자로 받음
  methods: {
    deleteTodo(){
      this.$store.dispatch('deleteTodo', this.todo)
    },
    // 6.
    updateTodo(){
      // console.log('updateTodo')
      this.$store.dispatch('updateTodo', this.todo)
    }
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
