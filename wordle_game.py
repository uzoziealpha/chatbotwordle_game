#program that guesses random words and interacts with the Wordle-like API provided. 
# The general steps of writing the code are as follows:
# API interacts 

import random
import requests
import json  # Import the json module for prettifying JSON

class WordleGame:
    def __init__(self):
        # API base URL for interacting with the Wordle-like game
        self.base_url = "https://wordle.votee.dev:8000/random"
        self.word_list = ["sogzd", "hello", "world"]  # Example word list

    def guess_word(self, guess: str, size: int = 5):
        """Simulate a guess against the daily puzzle."""
        url = f"{self.base_url}?guess={guess}&size={size}"
        response = requests.get(url)
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Pretty-print the JSON response using json.dumps with indent
            return json.dumps(response.json(), indent=4)  # Prettify the JSON output
        else:
            return {"error": "Unable to make a guess", "status_code": response.status_code}

    def guess_word_random(self, seed: int = None):
        """Generate a random guess from the word list and check it."""
        random.seed(seed)  # Set the seed for reproducibility (optional)
        random_word = random.choice(self.word_list)  # Choose a random word
        return self.guess_word(random_word)  # Check the random guess

# Example usage
if __name__ == "__main__":
    game = WordleGame()
    result = game.guess_word_random(seed=42)  # Pass a seed for reproducibility
    print(result)  # Print the pretty-printed result

    def guess_word_random(self, guess: str, seed: int = None):
        """Make a random guess against a randomly selected word from word_list."""
        random.seed(seed)  # Optional: Set the seed for reproducibility of the random guess
        random_word = random.choice(self.word_list)  # Pick a random word from the list
        return self.guess_word(random_word)  # Call guess_word with the random word