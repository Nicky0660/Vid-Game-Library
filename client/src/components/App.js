import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

// const baseURL = ('http://127.0.0.1:5555')

function App() {
  const [games, setGames] = useState([])
  
  useEffect(() => {
    fetch('http://127.0.0.1:5555/games')
      .then((res) => res.json())
      .then((data) => setGames(data));
  },[])
  console.log(games)

  return <h1>Gaming Library</h1>;
}


export default App;
