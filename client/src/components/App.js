import React, { useEffect, useState } from "react";
import { Switch, Route, BrowserRouter as Router } from "react-router-dom";
import NewGameForm from "./NewGameForm";
import SearchGame from "./SearchGame";
import GameDetail from "./GameDetail";
import GameList from "./GameList";
//import Header from "./Header";
//import Home from "./Home"
//Component imports 1-7

function App() {
  const [games, setGames] = useState([])
  
  useEffect(() => {
    fetch('http://127.0.0.1:5555/games')
      .then((res) => res.json())
      .then((data) => setGames(data));
  },[])
  console.log(games)

  return(
    <div>
      <header><h1>Random bullshit, GO!!</h1> </header>
      <Router>
        <Switch>
          <Route exact path="/">
            <h1>Gaming Library</h1>
            <GameList games={games} />
          </Route>
          <Route path="/add-game">
            <NewGameForm/>
          </Route>
          <Route path="/game-detail/:id">
            <GameDetail games={games} />
          </Route>
          <Route path="/search-game">
            <SearchGame/>
          </Route>
        </Switch>
      </Router>
    </div>
  )
  // return (
  // <>
  //   <h1>Gaming Library</h1>
  //   <></>
  //   <h2>Make your selection</h2>
  //   <Navbar>
  //     <Switch>
  //       <Route exact path = '/'>
        
  //       </Route>
  //     </Switch>
  //   </Navbar>
  // </>
  // )
};


export default App;
