import React, {useState, Fragment} from "react";
import {useHistory} from "react-router-dom"


// import { Form } from "semantic-ui-react";

function NewGameForm({setGames, consoles}) {
  const [title, setTitle] = useState("");
  const [releaseYr, setReleaseYr] = useState("");
  const [genre, setGenre] = useState("");
  const [img, setImg] = useState("");
  const [consoleIds, setConsoleIds] = useState("");

  const history = useHistory()

  const handleSubmit = (e) => {
    e.preventDefault();

    const gameForm = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        "genre_id": parseInt(genre),
        "release_yr": parseInt(releaseYr),
        img,
        "console_ids": consoleIds
      }),
    };

    fetch("http://127.0.0.1:5555/games", gameForm)
      .then((res) => res.json())
      .then((data) => {
        setGames( games => [ ...games , data ])
        history.push('/games')
      })

    setTitle("");
    setGenre("");
    setConsoleIds([]);
    setReleaseYr("")
  };

    function handleSelectConsole(e){
        setConsoleIds(consoleIds => [...consoleIds,e.target.value])
    }

    const consoleSelector = () => {
        return consoles.map(console => (
            <Fragment key = {console.id}>
            <input
                onClick={handleSelectConsole} 
                type = "checkbox"
                name = {console.name}
                value = {console.id}
                id = {console.name}
            />
            <label htmlFor={console.name}>{console.name}</label>
            </Fragment>
        ))
    }



  return (
    <div>
      <h3>Add a Game!</h3>
      <form onSubmit={handleSubmit}>
        <input
          label="Title"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          label="Genre"
          placeholder="Genre ID#"
          value={genre}
          onChange={(e) => setGenre(e.target.value)}
        />
        {consoleSelector()}
        <input
          label="release_yr"
          placeholder="Enter release year"
          value={releaseYr}
          onChange={(e) => setReleaseYr(e.target.value)}
        />
         <input
          label="Image"
          placeholder="Image URL"
          value={img}
          onChange={(e) => setImg(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default NewGameForm;