# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader


class TestJsonDataReader:
    @pytest.fixture()
    def valid_json_data(self) -> tuple[str, DataType]:
        json_string = """
        {
            "Иванов Иван Иванович": [
                ["математика", 80],
                ["программирование", 90],
                ["литература", 76]
            ],
            "Петров Петр Петрович": [
                ["математика", 100],
                ["социология", 90],
                ["химия", 61]
            ]
        }
        """
        expected_data = {
            "Иванов Иван Иванович": [
                ["математика", 80],
                ["программирование", 90],
                ["литература", 76]
            ],
            "Петров Петр Петрович": [
                ["математика", 100],
                ["социология", 90],
                ["химия", 61]
            ]
        }
        return json_string, expected_data

    @pytest.fixture()
    def filepath_and_data(self, valid_json_data: tuple[str, DataType], tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("data.json")
        p.write_text(valid_json_data[0], encoding='utf-8')
        return str(p), valid_json_data[1]

    def test_read_valid_json(self, filepath_and_data: tuple[str, DataType]) -> None:
        reader = JsonDataReader()
        data = reader.read(filepath_and_data[0])
        assert data == filepath_and_data[1]

    def test_read_invalid_json(self, tmpdir) -> None:
        p = tmpdir.mkdir("datadir").join("invalid.json")
        p.write_text("This is not valid JSON", encoding='utf-8')
        reader = JsonDataReader()
        data = reader.read(str(p))
        assert data == {}

    def test_read_invalid_json_structure(self, tmpdir) -> None:
        p = tmpdir.mkdir("datadir").join("invalid_structure.json")
        p.write_text('{"student1": "wrong data"}', encoding='utf-8')  # не list
        reader = JsonDataReader()
        data = reader.read(str(p))
        assert data == {}

    def test_read_nonexistent_file(self) -> None:
        reader = JsonDataReader()
        data = reader.read("/test_data/nonexistent_file.json")
        assert data == {}
