# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JsonDataReader import JsonDataReader
from QuartileCalc import QuartileCalc


def get_path_and_format_from_arguments(args) -> tuple[str, str]:
    parser = argparse.ArgumentParser(description="Path "
                                                 "to datafile and data format")
    parser.add_argument("-p", dest="path",
                        type=str, required=True, help="Path to datafile")
    parser.add_argument("-f", dest="format",
                        type=str, default="txt", choices=["txt", "json"],
                        help="Data format (txt or json)")
    args = parser.parse_args(args)
    return args.path, args.format


def main():
    path, data_format = get_path_and_format_from_arguments(sys.argv[1:])

    if data_format == "txt":
        reader = TextDataReader()
    elif data_format == "json":
        reader = JsonDataReader()
    else:
        raise ValueError("Unsupported data format")

    students = reader.read(path)

    if not students:
        print("Error reading data. Exiting.")
        return

    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    quartile_students = QuartileCalc(rating).calc()
    print("Students in the last quartile:", quartile_students)


if __name__ == "__main__":
    main()
