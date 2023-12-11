<template>
  <div>
    <!-- 3. -->
    <TodoListItem v-for="(todo, index) in todos" :key="index" :todoitem="todo"/>
  </div>
</template>

<script>
// 1.
import TodoListItem from './TodoListItem.vue'

export default {
  name: 'TodoList',
  components: {
    // 2.
    TodoListItem,
  },
  computed: {
    todos(){
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>