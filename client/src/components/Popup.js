import React from 'react';

function PopUp({ onClose }) {

  return (
    <div className="popup">
      <div className="popup-content">
        <h2>What Our Website Can Do</h2>
        <ul>
          <li>Im about to insert a bunch of random information here just so we can see the scaling if we did this in list format</li>
          <li>Im about to insert a bunch of random information here just so we can see the scaling if we did this in list format</li>
          <li>Im about to insert a bunch of random information here just so we can see the scaling if we did this in list format</li>
        </ul>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

export default PopUp;
