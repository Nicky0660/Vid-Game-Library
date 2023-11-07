import React, { useEffect, useState } from "react";
import Games from "./Games"
import NavBar from "./NavBar"
import { Switch, Route } from "react-router-dom";
import PopUp from "./Popup";
import Genres from "./Genres";

// const baseURL = ('http://127.0.0.1:3000')

function App() {
  const [games, setGames] = useState([])
  const[consoles, setConsoles]= useState([])
  const[genres, setGenres]= useState([])
  const [isPopUpOpen, setPopUpOpen] = useState(false);
  
  const closePopUp = () => {
    setPopUpOpen(false);
  };

  useEffect(() => {
    setPopUpOpen(true);
  }, []);

  useEffect(() => {
    fetch('http://127.0.0.1:3000/games')
      .then((res) => res.json())
      .then((data) => setGames(data))
  },[])
  //console.log(data)


  useEffect(() => {
    fetch('http://127.0.0.1:3000/consoles')
      .then((res) => res.json())
      .then((data) => setConsoles(data))
  },[])
  //console.log(data)

  useEffect(() => {
    fetch('http://127.0.0.1:3000/genres')
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
        <Games games={games}/>
      </Route>
      <Route exact path="/genres">
        <Genres genres={genres}/>
      </Route>
      <Route exact path="/games">
      </Route>
    </Switch>
    <div className="App">
      {isPopUpOpen && <PopUp onClose={closePopUp} />}
      <div className="landing-page">
        {/* Your landing page content goes here */}
      </div>
    </div>
  </>
  );
}



export default App;
