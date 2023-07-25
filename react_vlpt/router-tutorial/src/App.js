import React from "react";
import { Route, Routes, Link  } from "react-router-dom";
import Home from "./Home";
import About from "./About";
// import Profile from "./Profile";
import Profiles from "./Profiles";

const App = () => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/about">소개</Link>
        </li>
        <li>
          <Link to="/profiles">프로필목록</Link>
        </li>
      </ul>
      <hr />
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/about" element={<About/>} />
        {/* <Route path="/profile/:username" element={<Profile/>} /> */}
        <Route path="/profiles/*" element={<Profiles/>} />
      </Routes>
    </div>
  )
}

export default App