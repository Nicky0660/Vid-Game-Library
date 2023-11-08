import React from "react";
import ConsoleDetail from "./ConsoleDetails";

function Consoles({consoles}){
    const mappedConsoles = consoles.map(console =>(
        <ConsoleDetail
            key={console.id}
            name={console.name}
            img={console.img}
        />
    ))
    return (
    <div className="console-container">{mappedConsoles}</div>
    )
}
export default Consoles