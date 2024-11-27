#!/usr/bin/node


const request = require('request');
//
//const movieId = process.argv[2];
//
//const url = 

// Function to fetch and print characters from the Star Wars API
function getStarWarsCharacters(movieId) {
  // Make a GET request to the /films/{id}/ endpoint to fetch movie data
  request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, function(error, response, body) {
    // If there's an error or if the movie ID is invalid, return
    if (error) {
      console.error("Request error:", error);
      return;
    }
    
    // If the response status is not 200, print an error
    if (response.statusCode !== 200) {
      console.log("Error: Movie not found.");
      return;
    }

    // Parse the movie data
    const movieData = JSON.parse(body);

    // Check if the movie has a characters list, if not, handle accordingly
    if (!movieData.characters || movieData.characters.length === 0) {
      console.log("No characters found for this movie.");
      return;
    }

    // Extract the list of character URLs
    const characterUrls = movieData.characters;

    // Fetch each character's details and print their name
    characterUrls.forEach(function(url) {
      request(url, function(error, response, body) {
        if (error) {
          console.error("Error fetching character:", error);
          return;
        }

        if (response.statusCode !== 200) {
          console.log("Error: Could not fetch character data.");
          return;
        }

        // Parse the character data and print the name
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        resolve()
      });
    });
  });
}

// Check if the script is called with the correct number of arguments
if (process.argv.length !== 3) {
  console.log("Usage: ./0-starwars_characters.js <movie_id>");
  process.exit(1);
}

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Validate if the movie ID is a valid number
if (isNaN(movieId)) {
  console.log("Error: Movie ID must be an integer");
  process.exit(1);
}

// Call the function to fetch characters for the given movie ID
getStarWarsCharacters(movieId);