import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import React, { useState } from 'react';
import SearchBar from './SearchBar';

function NavBar({onSearch}){
    // use state hook setting up a nav bar toggle
    const [isOpen, setIsOpen] = useState(false);
    const toggleNav = () => {
        setIsOpen(!isOpen);
    }
    return(
    <div>
        {/* added button for on click event */}
        <div className="toggleButton">
            <button onClick={toggleNav}>Initialize</button>
            <SearchBar onSearch={onSearch} /> {/* Pass onSearch function as prop */}
        </div>
        {/* If isOpen state true, class open is applied. If isOpen false, then no class applied. */}
        <div className ={`navBar ${isOpen ? 'open' : 'hidden'}`}>
            

           <NavLink  to="/games" > Game List </NavLink>
           
           <NavLink  to="/genres" >  Genre List  </NavLink>
           
           <NavLink  to="/consoles" > Console List  </NavLink>
           
           <NavLink to="/newGame"> Enter New Game </NavLink>
        </div>
    </div>
    )
}
export default NavBar;