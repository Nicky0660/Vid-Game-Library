import React from "react";
import GenreDetails from './GenreDetails.js'

function Genres({genres}){
    const mappedGenres = genres.map(genre => (
        <GenreDetails
            key={genre.id}
            id={genre.id}
            name={genre.name}
        />
    ))
    return (
    <div className="genre-container">{mappedGenres}</div>
    )
}
export default Genres