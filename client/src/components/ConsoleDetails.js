import React from "react";

function ConsoleDetails({name, img}){

    return (
        <div className = 'console-details'>
            <h3 className="console-name">{name}</h3>
            <img className="console-img" src={img} alt={name}/>
        </div>
    )
}
export default ConsoleDetails