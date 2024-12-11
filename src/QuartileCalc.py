# src/QuartileCalc.py
from src.Types import DataType, RatingType

class QuartileCalc:
    def __init__(self, rating: RatingType) -> None:
        self.rating = rating

    def calc(self) -> list[str]:
        if not self.rating:
            return []

        sorted_ratings = sorted(self.rating.values())
        n = len(sorted_ratings)

        if n < 4:
            q3 = sorted_ratings[-1]
        else:
            q3_index = 3 * n // 4
            q3 = sorted_ratings[q3_index]

        last_quartile_students = [
            student for student, rating in self.rating.items() if rating >= q3
        ]
        return last_quartile_students