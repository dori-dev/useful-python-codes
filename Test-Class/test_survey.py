"""Test Survey Codes
"""
import unittest
from survey import AnonymousSurvey


class TestSurvey(unittest.TestCase):
    """Tests for AnonymousSurvey class
    """

    def setUp(self):
        """Create Instance from AnonymousSurvey and
        Set up any codes for use in any test methods
        """
        question = "Which city do you want to visit most?"
        self.my_survey = AnonymousSurvey(question)

    def test_store_single_response(self):
        """Test that a single response is stored properly
        """
        # Initialize
        self.my_survey.store_response("Salar", "Shiraz")
        # Assert
        self.assertIn("Shiraz", self.my_survey.responses.values())

    def test_store_three_respones(self):
        """Test that a three responses is stored properly
        """
        # Initialize
        names = ["Mohammad", "Dori", "Amir"]
        responses = ["NewYork", "Paris", "Tehran"]
        for name, response in zip(names, responses):
            self.my_survey.store_response(name, response)
        # Asserts
        for response in responses:
            self.assertIn(response, self.my_survey.responses.values())
        self.assertEqual(dict(zip(names, responses)), self.my_survey.responses)

    def test_statistics(self):
        """Test the statistics of Survey class
        """
        # Initialize
        names = [
            "Salar", "Ali", "Mohammad", "Dori", "Jack", "Joe"
        ]
        responses = [
            "NewYork", "Tehran", "NewYork", "Paris", "Tehran", "NewYork"
        ]
        for name, response in zip(names, responses):
            self.my_survey.store_response(name, response)
        # Asserts
        statistics = self.my_survey.show_statistics()
        responses = ["NewYork", "Paris", "Tehran"]
        results = [3, 1, 2]
        for response, result in zip(responses, results):
            self.assertEqual(statistics[response], result)


if __name__ == "__main__":
    unittest.main()
