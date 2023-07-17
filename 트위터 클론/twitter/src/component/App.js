import React, {useState} from "react";
import AppRouter from "./Router";

function App() {
  const [isLoggedIn, setIsLoggendIn] = useState(true)

  return (
      <AppRouter isLoggedIn={isLoggedIn}/>
  );
}

export default App;
