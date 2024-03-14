import React from 'react';

function PopUp({ onClose }) {

  return (
    <div className="popup">
      <div className="popup-content">
        <h2>Video Game Library</h2>
        <ul>
          <li>Here you can view the library as a whole from Game List</li>
          <li>Hit Initialize to view the NavBar and make a selection</li>
          <li>You can edit or delete a game from the Game List</li>
          <li>Create a new Game by selecting the Enter New Game button</li>
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-RMZlZi6i_zZQlpo2x6cV_ZbL498LNbLxkg&usqp=CAU"/>
        </ul>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

export default PopUp;