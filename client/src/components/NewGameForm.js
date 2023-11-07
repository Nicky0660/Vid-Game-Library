import React, {useState} from "react";

import { useState } from "react";
import { Form } from "semantic-ui-react";

function NewGameForm({setIsData}) {
  const [title, setTitle] = useState("");
  const [genre, setGenre] = useState("");
  const [platform, setPlatform] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    const gameForm = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        genre,
        platform,
      }),
    };

    fetch("http://127.0.0.1:5555/games", gameForm)
      .then((res) => res.json())
      .then((data) => {
    //    setIsData( => [ , ])
       console.log(data)
      })

    setTitle("");
    setGenre("");
    setPlatform("");
  };

  return (
    <div>
      <h3>Add a Game!</h3>
      <Form onSubmit={handleSubmit}>
        <Form.Input
          fluid
          label="Title"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <Form.Input
          fluid
          label="Genre"
          placeholder="Genre"
          value={genre}
          onChange={(e) => setGenre(e.target.value)}
        />
        <Form.Input
          fluid
          label="Platform"
          placeholder="Platform"
          value={platform}
          onChange={(e) => setPlatform(e.target.value)}
        />
        <Form.Button type="submit">Submit</Form.Button>
      </Form>
    </div>
  );
}

export default NewGameForm;