import unittest
from unittest.mock import patch
from wordle_game import WordleGame

class TestWordleGame(unittest.TestCase):
    
    @patch("requests.get")  # Mock the requests.get function
    def test_guess_word(self, mock_get):
        """Test the guess_word method."""
        mock_response = {
            "slot": 0,
            "guess": "h",
            "result": "absent"
        }
        mock_get.return_value.status_code = 200  # Mock a successful response
        mock_get.return_value.json.return_value = [mock_response]  # Mock the JSON response
        
        game = WordleGame()
        response = game.guess_word("hello")
        
        # Assert the response matches the mock data
        self.assertEqual(response, [mock_response])
        mock_get.assert_called_once_with("https://wordle.votee.dev:8000/random?guess=hello&size=5")
    
    @patch("requests.get")  # Mock the requests.get function
    def test_guess_word_random(self, mock_get):
        """Test the guess_word_random method with random word selection."""
        mock_response = {
            "slot": 0,
            "guess": "s",
            "result": "absent"
        }
        mock_get.return_value.status_code = 200  # Mock a successful response
        mock_get.return_value.json.return_value = [mock_response]  # Mock the JSON response
        
        game = WordleGame()
        response = game.guess_word_random("hello")
        
        self.assertEqual(response, [mock_response])
        mock_get.assert_called_once()  # Ensure the GET request was made

if __name__ == "__main__":
    unittest.main()