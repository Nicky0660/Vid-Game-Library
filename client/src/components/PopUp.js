import React from 'react';

function PopUp({ onClose }) {

  return (
    <div className="popup">
      <div className="popup-content">
        <h2>Here is Game Library</h2>
        <ul>
          <li>Here you can view the library as a whole from Game List</li>
          <li>Enter New Game using an integer for Genre id correspondent to the list found in Genre List</li>
          <li>From Console List highlight each console to see which games are available for that Console!</li>
        </ul>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

export default PopUp;