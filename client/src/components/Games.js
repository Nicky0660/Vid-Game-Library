import React from "react";
import Games from "games"

function GameList({games}){
    const mappedArrray = games.map(game =>(
       <Games 
       key={game.id}
       name={game.name}
       releaseYr={game.releaseYr}
       genre={game.genre}
       />
        
    ))
}