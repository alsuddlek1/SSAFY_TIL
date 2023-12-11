import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
    ]
  },
  getters: {
    alltodosCount(state){
      return state.todos.length
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    // 4. 
    DELETE_TODO(state, todoItem){
      // console.log(todoItem) // 삭제 버튼 누른 todo clwdltk state.todos에서 삭제
      const index = state.todos.indexOf(todoItem)
      // splice(a,b) : index a부터 b개 삭제
      state.todos.splice(index, 1)
    },
    // 8.
    UPDATE_TODO(state,todoItem){
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) { // 내가 클릭한 todo item을 state.todos 배열에서 찾아서,
          todo.isCompleted = !todo.isCompleted // todo item의 isCompleted를 뒤집는다
        }
        return todo
      })
      // 함수 -> state.todos 배열에서 클릭한 todo item 찾고 해당 todo,isComplted를 
      // 반대로 뒤집는다. ture -> false
    },
    LOAD_TODOS(state){
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)

      state.todos = parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // console.log(context)
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    // 3. DELETE_TODO 뮤테이션 생성, todoItem 넘겨줌
    deleteTodo(context, todoItem){
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    }, 
    // 7.
    updateTodo(context, todoItem){
      context.commit('UPDATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    // 수정할때마다 저장할거니까 actions에서
    saveTodosToLocalStorage(context){
      const jsonTodos = JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    },
    loadTodos(context) {
      context.commit('LOAD_TODOS')
    }
  },
  modules: {
  }
})
