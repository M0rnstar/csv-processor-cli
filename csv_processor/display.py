from typing import List, Dict, Any
from tabulate import tabulate


def print_table(data: List[Dict[str, Any]]) -> None:
    if not data:
        print("Нет данных для отображения.")
        return

    print(tabulate(data, headers="keys", tablefmt="grid"))
