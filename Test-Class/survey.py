"""Python Survey
"""
from collections import Counter


class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = {}

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, name, new_response):
        """Store a single response to the survey."""
        self.responses[name] = new_response

    def show_statistics(self):
        """Show statistics of responses
        """
        statistics = Counter(self.responses.values())
        return dict(statistics)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for name, response in self.responses.items():
            print(f"- {name}: {response}")
        print(self.show_statistics())


if __name__ == "__main__":
    QUESTION = "Which city do you want to visit most?"
    my_survey = AnonymousSurvey(QUESTION)
    my_survey.show_question()
    my_survey.store_response("Mohammad", "NewYork")
    my_survey.store_response("Salar", "Tehran")
    my_survey.store_response("Dori", "Paris")
    my_survey.show_results()
