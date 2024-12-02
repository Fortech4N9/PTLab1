# -*- coding: utf-8 -*-
from src.main import get_path_and_format_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], str, str]:
    return (["-p", "/home/user/file.txt", "-f", "json"],
            "/home/user/file.txt", "json")


@pytest.fixture()
def correct_arguments_string_default_format() -> tuple[list[str], str, str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.txt", "txt"


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


@pytest.fixture()
def incorrect_format_arguments() -> list[str]:
    return ["-p", "/home/user/file.txt", "-f", "invalid"]


def test_get_path_and_format_from_correct_arguments(
        correct_arguments_string: tuple[list[str], str, str]) -> None:
    path = get_path_and_format_from_arguments(correct_arguments_string[0])
    data_format = path
    assert path == correct_arguments_string[1]
    assert data_format == correct_arguments_string[2]


def test_get_path_with_default_format(
        correct_arguments_string_default_format: tuple[list[str], str, str])\
        -> None:
    path = get_path_and_format_from_arguments(
        correct_arguments_string_default_format[0])
    data_format = path
    assert path == correct_arguments_string_default_format[1]
    assert data_format == correct_arguments_string_default_format[2]


def test_get_path_from_noncorrect_arguments(
        noncorrect_arguments_string: list[str]) -> None:
    with pytest.raises(SystemExit):
        get_path_and_format_from_arguments(noncorrect_arguments_string)


def test_incorrect_format_argument(incorrect_format_arguments: list[str]) \
        -> None:
    with pytest.raises(SystemExit):
        get_path_and_format_from_arguments(incorrect_format_arguments)
