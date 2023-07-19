import React from "react"
import {createGlobalStyle }  from 'styled-components'
import TodoTemplate from "./components/TodoTemplate";
import TodoHead from "./components/TodoHead"
import TodoList from "./components/TodoList";
import TodoCreate from "./components/TodoCreate"
import TodoProvide from "./components/TodoProvider"

const GlobalStyle = createGlobalStyle`
  body {
    background : #e9ecef
  }
`;

function App() {
  return (
    <div>
      <TodoProvide>
      <GlobalStyle/>
      <TodoTemplate>
        <TodoHead/>
        <TodoList/>
        <TodoCreate/>
      </TodoTemplate>
      </TodoProvide>
    </div>
  );
}

export default App;
