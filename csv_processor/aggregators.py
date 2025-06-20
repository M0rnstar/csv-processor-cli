from typing import List, Dict, Any, Callable


def average(values: List[float]) -> float:
    if not values:
        raise ValueError("Невозможно вычислить среднее по пустому списку")
    return sum(values) / len(values)


def apply_aggregation(data: List[Dict[str, Any]], aggregate_expr: str) -> float:
    operations: Dict[str, Callable[[List[float]], float]] = {
        "avg": average,
        "min": min,
        "max": max,
    }

    if ":" not in aggregate_expr:
        raise ValueError(f"Агрегация должна быть в формате операция:колонка, напр. avg:price")

    operation_name, column = aggregate_expr.split(":", 1)
    operation_name, column = operation_name.strip(), column.strip()

    if operation_name not in operations:
        raise ValueError(f"Агрегация '{operation_name}' не поддерживается")

    operation = operations[operation_name]

    values = [
        row[column]
        for row in data
        if column in row and isinstance(row[column], (int, float))
    ]

    if not values:
        raise ValueError(f"Нет числовых значений в колонке '{column}'")

    return operation(values)
