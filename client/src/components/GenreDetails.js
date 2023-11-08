import React from "react";

function GenreDetails({name,id}){

    return(
        <div className="genre-details">
            <h3 className="genre-name">{name} = {id}</h3>
        </div>

    )
}
export default GenreDetails
