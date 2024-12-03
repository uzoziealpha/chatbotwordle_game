#program that guesses random words and interacts with the Wordle-like API provided. 
# The general steps of writing the code are as follows:


import random
import requests

class WordleGame:
    def __init__(self):
        # The base URL of the Wordle API
        self.base_url = "https://wordle.votee.dev:8000"
        self.word_list = ["sogzd", "hello", "world"]  # Example word list for random guesses

    def guess_word(self, guess: str):
        """Send a guess to the API and receive the response."""
        url = f"{self.base_url}/random?guess={guess}&size=5"
        response = requests.get(url)  # Send GET request with the guess
        
        if response.status_code == 200:
            return response.json()  # Return the response as JSON if successful
        else:
            return {"error": "Unable to make a guess", "status_code": response.status_code}

    def guess_word_random(self, guess: str, seed: int = None):
        """Make a random guess against a randomly selected word from word_list."""
        random.seed(seed)  # Optional: Set the seed for reproducibility of the random guess
        random_word = random.choice(self.word_list)  # Pick a random word from the list
        return self.guess_word(random_word)  # Call guess_word with the random word