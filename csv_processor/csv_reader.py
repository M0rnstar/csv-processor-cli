import csv
from typing import List, Dict, Any


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []

        for row in reader:
            converted_row = {}
            for key, value in row.items():
                value = value.strip()

                if value.replace(".", "", 1).isdigit():
                    converted_row[key] = float(value) if "." in value else int(value)
                else:
                    converted_row[key] = value

            rows.append(converted_row)

        return rows
