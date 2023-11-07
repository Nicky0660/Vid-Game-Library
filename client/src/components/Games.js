import React from "react";
import GameDetail from"./GameDetail";

function Games({games}){
    console.log(games)
    const mappedArray = games.map(game =>(
       <GameDetail 
       key={game.id}
       title={game.title}
       releaseYr={game['release_yr']}
       genre={game.genre.name}
       img={game.img}

       />
        
    ))
    return (
       <>{mappedArray} </>
    )
}
export default Games