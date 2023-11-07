import React from "react";

function Games({games}){
    const mappedArrray = games?.map(game =>(
       <Games 
       key={game.id}
       name={game.name}
       releaseYr={game.releaseYr}
       genre={game.genre}
       />
        
    ))
}
export default Games;
