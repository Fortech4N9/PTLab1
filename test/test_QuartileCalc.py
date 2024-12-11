from src.Types import RatingType
from src.QuartileCalc import QuartileCalc
import pytest


class TestQuartileCalc:
    @pytest.mark.parametrize(
        "rating, expected_students",
        [
            ({"student1": 50, "student2": 60, "student3": 70, "student4": 80}, ["student4"]),
            ({"student1": 80, "student2": 70, "student3": 60, "student4": 50}, ["student1"]),
            ({"student1": 50, "student2": 60, "student3": 70}, ["student3"]), # < 4 элементов
            ({"student1": 50, "student2": 60}, ["student2"]), # < 4 элементов
            ({}, []), # пустой рейтинг
            ({"student1": 50, "student2": 50, "student3": 50, "student4": 50}, ["student1", "student2", "student3", "student4"]), # все одинаковые
            ({"student1": 70, "student2": 80, "student3": 90, "student4": 100, "student5": 60}, ["student3", "student4"]), # > 4 элементов
            ({"student1": 70, "student2": 70, "student3": 90, "student4": 100}, ["student4"]), # > 4 элементов,  дубликаты
        ]
    )

    def test_calc(self, rating: RatingType, expected_students: list[str]) -> None:
        quartile_calc = QuartileCalc(rating)
        students = quartile_calc.calc()
        assert sorted(students) == sorted(expected_students)  # сравниваем отсортированные списки