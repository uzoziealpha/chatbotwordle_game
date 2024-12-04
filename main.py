import json
from wordle_game import WordleGame  # Import the WordleGame class from wordle_game.py

if __name__ == "__main__":
    game = WordleGame()  # Create an instance of the WordleGame class
    
    print("Testing random guess:")
    result = game.guess_word_random()  # Make a random guess from the word list
    print(json.dumps(result, indent=4))  # Pretty print the API response with indentation for better readability