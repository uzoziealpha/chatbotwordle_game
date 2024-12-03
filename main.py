from wordle_game import WordleGame

def main():
    game = WordleGame()
    
    # Simulate a random guess (this could be more dynamic based on the game flow)
    guess = "hello"  # Example guess
    print(f"Generated word: {guess}")
    
    # Make a guess against the random word
    response = game.guess_word(guess)
    print("API Response:", response)

if __name__ == "__main__":
    main()
    

    
