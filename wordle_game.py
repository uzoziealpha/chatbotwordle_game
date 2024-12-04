#program that guesses random words and interacts with the Wordle-like API provided. 
# The general steps of writing the code are as follows:
# API interacts 

import random
import requests
import json

class WordleGame:
    def __init__(self):
        # API base URL for interacting with the Wordle-like game
        self.base_url = "https://wordle.votee.dev:8000/random"  # Endpoint for random guesses
        self.word_list = ["sogzd", "hello", "world", "apple", "grape", "peach", "lemon"]  # Example list of words

    def guess_word(self, guess: str, size: int = 5):
        """Simulate a guess against the random word."""
        url = f"{self.base_url}?guess={guess}&size={size}"
        response = requests.get(url)  # Send GET request to the API
        
        if response.status_code == 200:
            return response.json()  # Return the JSON response from the API
        else:
            return {"error": "Unable to make a guess", "status_code": response.status_code}

    def guess_word_random(self, seed: int = None):
        """Generate a random guess from the word list and check it."""
        random.seed(seed)  # Set the seed for reproducibility (optional)
        random_word = random.choice(self.word_list)  # Select a random word from the list
        return self.guess_word(random_word)  # Check the random guess against the API