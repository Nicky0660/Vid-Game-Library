import React, { useEffect, useState } from "react";

import NavBar from "./NavBar"
import { Switch, Route } from "react-router-dom";
import Home from "./Home"


// const baseURL = ('http://127.0.0.1:5555')

function App() {
  const [gamesArray, setGamesArray] = useState([])
  const[consoles, setConsoles]= useState([])
  const[genres, setGenres]= useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5555/games')
      .then((res) => res.json())
      .then((data) => setGamesArray(data))
  },[])
  //console.log(data)


  useEffect(() => {
    fetch('http://127.0.0.1:5555/consoles')
      .then((res) => res.json())
      .then((data) => setConsoles(data))
  },[])
  //console.log(data)

  useEffect(() => {
    fetch('http://127.0.0.1:5555/genres')
      .then((res) => res.json())
      .then((data) => setGenres(data))
    },[])
  
  return (
    <>
    <header>
      <h1>Game Library</h1>
    </header>
    <NavBar/>
    <Switch>
      <Route exact path="/">
        <Home gamesArray={gamesArray}/>
      </Route>
      <Route exact path="/games">
        
      </Route>
    </Switch>
    </>
 
  
  
  
  
  );

}



export default App;
