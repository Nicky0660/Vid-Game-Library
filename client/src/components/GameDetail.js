import React from "react";


function GameDetail({title, releaseYr, genre, img}){
    return( <>
    <h3 className="game-title">{title}</h3>
    <img className="game-img" src={img} alt={title}/>
    <p className="game-genre">{genre}</p>
    <p className="game-release_yr">{releaseYr}</p>

    </>)
}
export default GameDetail