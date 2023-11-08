import React, { useState, Fragment }from "react";



// const reviseGame = {
//     method: "PATCH",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       title,
//       "genre_id": parseInt(genre),
//       "release_yr": parseInt(releaseYr),
//       img,
//       "console_ids": consoleIds
//     }),
//   };



function GameDetail({title, releaseYr, genre, img, game, consoles}){

    const [showEditForm, setShowEditForm] = useState(false)
    const [editTitle, setEditTitle] = useState(title);
    const [editReleaseYr, setEditReleaseYr] = useState(releaseYr);
    const [editGenre, setEditGenre] = useState(genre);
    const [editImg, setEditImg] = useState(img);
    const currentConsoleIds =  game['console_games'].map(g=>g['console_id'])
    
    const [consoleIds, setConsoleIds] = useState(currentConsoleIds);

    function handleSelectConsole(e){
        setConsoleIds(consoleIds => [...consoleIds,e.target.value])
    }

    const handleSubmit = (e) => {
        e.preventDefault();
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
                checked = {consoleIds.includes(console.id)}
                
            />
            <label htmlFor={console.name}>{console.name}</label>
            </Fragment>
        ))
    }
    
    if (showEditForm){
        return (
            <div>
                <h3>Edit a Game!</h3>
                <form onSubmit={handleSubmit}>
                    <input
                    label="Title"
                    placeholder="Title"
                    value={editTitle}
                    onChange={(e) => setEditTitle(e.target.value)}
                    />
                    <input
                    label="Genre"
                    placeholder="Genre"
                    value={editGenre}
                    onChange={(e) => setEditGenre(e.target.value)}
                    />
                    {consoleSelector()}
                    <input
                    label="release_yr"
                    placeholder="release_yr"
                    value={editReleaseYr}
                    onChange={(e) => setEditReleaseYr(e.target.value)}
                    />
                    <input
                    label="Image"
                    placeholder="Image"
                    value={editImg}
                    onChange={(e) => setEditImg(e.target.value)}
                    />
                    <button type="submit">Submit</button>
                </form>
            </div>
        )
    }

    return( <div className = 'game-card'>
    <h3 className="game-title">{title}</h3>
    <img className="game-img" src={img} alt={title}/>
    <p className="game-genre">{genre}</p>
    <p className="game-release_yr">{releaseYr}</p>
    <button onClick = { () => setShowEditForm(!showEditForm)}> Edit Game </button>

    </div>)
}
export default GameDetail