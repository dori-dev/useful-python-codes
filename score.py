"""Work with scores
"""
from typing import List


class Score:
    """Score class for work with any socres
    """

    def __init__(self, scores: List[int]):
        self.scores: list = scores

    def first_score(self) -> int:
        """get first score of scores

        Returns:
            int: first score
        """
        return self.scores[0]

    def last_score(self) -> int:
        """get last score of scores

        Returns:
            int: last score
        """
        return self.scores[-1]

    def score_average(self) -> int:
        """get average of scores

        Returns:
            int: average score
        """
        score_sum: int = sum(self.scores)
        score_length: int = len(self.scores)
        return round(score_sum/score_length, 2)

    @staticmethod
    def __get_n_largest_socres(scores: List[int], number: int) -> List[int]:
        """get any(n) largest scores in `scores` list

        Args:
            scores (List[int]): list of scores
            number (int): some socres

        Returns:
            List[int]: n largest scores list
        """
        sorted_scores: list = sorted(scores, reverse=True)
        return sorted_scores[:number]

    def top_3_scores(self) -> List[int]:
        """get 3 best(large) scores

        Returns:
            List[int]: list of 3 best score
        """
        return self.__get_n_largest_socres(self.scores, 3)

    def __repr__(self):
        return f"Scores: {str(self.scores)}"


if __name__ == "__main__":
    my_scores: object = Score([17, 18, 14, 13, 20, 19, 11, 18])
    print(my_scores)
    print(my_scores.first_score())
    print(my_scores.last_score())
    print(my_scores.score_average())
    print(my_scores.top_3_scores())
