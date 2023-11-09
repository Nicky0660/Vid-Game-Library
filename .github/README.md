# Game Library Website
Overview
This repository contains the code for a full-stack game library website. The purpose of this project is to create a centralized platform to store and manage information about various games, including details like the consoles they are available on, the release year, and the genre.

## Features

### Search Functionality:

Users can search for games by title, making it easy to find specific entries in the library.

### Add New Games: 
There's a user-friendly form for adding new games to the library. The Genre id must be utilized to input the correct genre. Once submitted, the website automatically redirects to the updated library.

### Edit Game Information: 
Users can easily edit the information of existing games here you must also utilize the genre id which can be located in the genre id list, ensuring that the library stays up-to-date.

### Delete Games: 
Games can be removed from the library if needed.

### Navigation Bar: 
The website features a navigation bar with quick links to the game list, genre list, console list, and a form for adding new games.

# Getting Started

### Prerequisites

- Ensure you have SQL installed on your system.

- Installation

- Clone the repository: git clone https://github.com/BootsRngr94/Phase_4_Proj_Vid-Game-Library.git

- Navigate to the project directory: cd Phase_4_Proj_Vid-Game-Library

## Set up the database:

- in a new terminal

- $pipenv install && pipenv shell 

- $cd server

- $flask db init

- $flask db commit -m 'initialize'

- $flask fb upgrade head

## Run the application: 
- in a new terminal 

- $cd client

- $npm install

- &npm start

## Seed database: 
- in a new terminal

- $pipenv shell

- $python server/seed.py

- Usage

- Access the website.

- Use the navigation bar to explore the game list, genre list, console list, or add a new game.

- Utilize the search functionality to find specific games.

## Fork the repository.
Create a new branch for your feature: git checkout -b feature-name

Commit your changes: git commit -m 'Add some feature'

Push to the branch: git push origin feature-name

Submit a pull request.

## Acknowledgments
Thanks to our amazing teachers Tyler and Eleanor for inspiration and guidance.

Feel free to customize it further based on your specific needs and preferences! :D