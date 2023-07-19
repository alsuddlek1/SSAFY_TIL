import React, {useReducer, createContext, useContext, useRef} from "react";

const initialTodos = [
    {
        id:1,
        text: ' 프로젝트 생성하기 ',
        done : true
    },
    {
        id: 2,
        text: '컴포넌트 스타일링하기',
        done: true
      },
      {
        id: 3,
        text: 'Context 만들기',
        done: false
      },
      {
        id: 4,
        text: '기능 구현하기',
        done: false
      }
]

// console.log(initialTodos) -> 잘나옴

function todoReducer(state, action) {
    // switch == if/elif/else 하지만 switch는 t/f가 아닌 case의 경우에 맞춰!
    switch (action.type){
        case 'CREATE':
            return state.concat(action.todo)
            // concat : 배열
            // create한 todo 항목을 기존 todo에 추가하여 업데이트
        case 'TOGGLE':
            return state.map(todo => 
                todo.id === action.id ? {...todo, done: !todo.done} : todo
                )
            // 같은 id를 찾고 상태를 변경해줌(t->f / f->t)
        case 'REMOVE':
            return state.filter(todo => todo.id !== action.id)
            // 같은 id를 제외하고 나머지 todo를 반환함
        default:
            // throw : JS에서 예외 발생
            throw new Error(`Unhandled action type : ${action.type}`)
    }
}

const TodoStateContext = createContext();
const TodoDispatchContext = createContext();
const TodoNextIdContext = createContext();

export function TodoProvider({children}){
    const [state, dispatch] = useReducer(todoReducer, initialTodos)
    const nextId = useRef(5)
    return (
        <TodoStateContext.Provider value={state}>
            <TodoDispatchContext.Provider value={dispatch}>
                <TodoNextIdContext.Provider value={nextId}>
                {children}
                </TodoNextIdContext.Provider>
            </TodoDispatchContext.Provider>
        </TodoStateContext.Provider>

    )
}

export function useTodoState() {
    return useContext(TodoStateContext);
  }
  
export function useTodoDispatch() {
    return useContext(TodoDispatchContext);
  }
  
export function useTodoNextId() {
    return useContext(TodoNextIdContext);
  }


// export default TodoContext