import React from "react";
import GameDetail from"./GameDetail";

function Games({games, consoles, setGames, genres}){
   //  console.log(games)
   if (!games) return null; 
    const mappedArray = games.map(game =>(
       <GameDetail 
       key={game.id}
       id={game.id}
       title={game.title}
       releaseYr={game['release_yr']}
       genre={game.genre.name}
       img={game.img}
       game = {game}
       consoles = {consoles}
       setGames = {setGames}
       games = {games}
       genres={genres}
       />
        
    ))

    
    return (
       <div className="card-container">{mappedArray} </div>
    )
}
export default Games
