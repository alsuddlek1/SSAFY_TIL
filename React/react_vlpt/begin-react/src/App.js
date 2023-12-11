import React, {useRef} from 'react';
import UserList from './UserList';
import './App.css';
import CreateUser from './CreateUser';


function App() {
  const name = 'react';
  const style = {
    backgroundColor: 'black',
    color: 'aqua',
    fontSize: 24, // 기본 단위 px
    padding: '1rem' // 다른 단위 사용 시 문자열로 설정
  }

  const users = [
    {
      id: 1,
      username: 'velopert',
      email: 'public.velopert@gmail.com'
    },
    {
      id: 2,
      username: 'tester',
      email: 'tester@example.com'
    },
    {
      id: 3,
      username: 'liz',
      email: 'liz@example.com'
    }
  ]

  const nextId = useRef(4)
  const onCreate = () => {
    // 나중에 구현 할 배열에 항목 추가하는 로직
  }

  nextId.current += 1
  return (
    <div>
      <CreateUser/>
      <UserList users={users} />
      
    </div>

  );
}

export default App;