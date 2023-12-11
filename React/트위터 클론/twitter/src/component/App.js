import React, {useState} from "react";
import AppRouter from "./Router";

function App() {
  const [isLoggedIn, setIsLoggendIn] = useState(true)

  return (
    <div>
      <AppRouter isLoggedIn={isLoggedIn}/>
      <footer>&copy; {new Date().getFullYear()}</footer>
    </div>
  );
}

export default App;
