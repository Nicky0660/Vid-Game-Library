import React from "react";
import GameDetail from"./GameDetail";

function Games({games, consoles}){
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
       />
        
    ))
    return (
       <>{mappedArray} </>
    )
}
export default Games
