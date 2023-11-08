import React from "react";
import GameDetail from"./GameDetail";

function Games({games, consoles, setGames}){
   //  console.log(games)
    const mappedArray = games.map(game =>(
       <GameDetail 
       key={game.id}
       title={game.title}
       releaseYr={game['release_yr']}
       genre={game.genre.name}
       img={game.img}
       game = {game}
       consoles = {consoles}
       setGames = {setGames}
       games = {games}
       />
        
    ))

    
    return (
       <div className="card-container">{mappedArray} </div>
    )
}
export default Games
