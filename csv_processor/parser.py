import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Обработка CSV-файла с фильтрацией и агрегацией"
    )

    parser.add_argument("--file", required=True, help="Путь к CSV-файлу")

    parser.add_argument(
        "--filter",
        help="Фильтрация в формате: column>value, column<value или column=value",
    )

    parser.add_argument(
        "--aggregate", help="Агрегация в формате: avg:column или max:column"
    )

    return parser.parse_args()
