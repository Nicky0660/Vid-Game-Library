import React from "react";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";



function NavBar(){
    return(
        <div className = 'navBar'>
           <NavLink  to="/games" > Game List </NavLink>
           
           <NavLink  to="/genres" >  Genre List  </NavLink>
           
           <NavLink  to="/consoles" > Console List  </NavLink>
           
           <NavLink to="/newGame"> Enter New Game </NavLink>
        </div>
    )
}
export default NavBar;