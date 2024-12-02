# -*- coding: utf-8 -*-
import json

from src.Types import DataType
from src.DataReader import DataReader


class JsonDataReader(DataReader):
    def read(self, path: str) -> DataType:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise TypeError("Invalid JSON format: Expected a dictionary at the top level.")
                for key, value in data.items():
                    if not isinstance(value, list):
                        raise TypeError(f"Invalid JSON format: Expected a list for student '{key}'.")
                    for item in value:
                        if not isinstance(item, list) or len(item) != 2 or not isinstance(item[0],
                                                                                          str) or not isinstance(
                                item[1], int):
                            raise TypeError(f"Invalid JSON format: Incorrect subject-score pair for student '{key}'.")

                return data

        except (FileNotFoundError, json.JSONDecodeError, TypeError) as e:
            print(f"Error reading or parsing JSON: {e}")
            return {}
