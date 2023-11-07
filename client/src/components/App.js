import React, { useEffect, useState } from "react";
import Games from './Games';
import NavBar from "./NavBar";
import { Switch, Route } from "react-router-dom";
import Genres from "./Genres";
import Consoles from "./Consoles";
import NewGameForm from "./NewGameForm";


// const baseURL = ('http://127.0.0.1:5555')

function App() {
  const [games, setGames] = useState([])
  const[consoles, setConsoles]= useState([])
  const[genres, setGenres]= useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5555/games')
      .then((res) => res.json())
      .then((data) => setGames(data))
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
      <Route exact path="/games">
        <Games games={games}/>
      </Route>
      <Route exact path="/genres">
        <Genres genres={genres}/>
      </Route>
      <Route exact path="/consoles">
        <Consoles consoles={consoles}/>
      </Route>
      <Route exact path="/newGame">
        <NewGameForm setGames={setGames} consoles={consoles}/>
      </Route>
    </Switch>
    </>
 
  
  
  
  
  );

}



export default App;
