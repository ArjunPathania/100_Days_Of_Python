import requests
from random import randint


class QuestionBank:
    def __init__(self, amount=10, category=None, difficulty="easy", question_type="boolean"):
        # Initialize default values and API request parameters
        self.category = category if category else randint(9, 32)
        self.parameters = {
            "amount": amount,
            "category": self.category,
            "difficulty": difficulty,
            "type": question_type
        }
        # Fetch question data on initialization
        self.question_data = self.fetch_data()
        # print(self.question_data)

    def fetch_data(self):
        """Fetch question data from the API and return JSON response."""
        response = requests.get("https://opentdb.com/api.php", params=self.parameters)
        response.raise_for_status()  # Handle any request errors
        return response.json().get("results", [])  # Return the "results" list of questions
