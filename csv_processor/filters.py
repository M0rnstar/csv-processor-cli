from typing import List, Dict, Any


def apply_filter(data: List[Dict[str, Any]], filter_expr: str) -> List[Dict[str, Any]]:
    if any(op in filter_expr for op in ["!=", ">=", "<="]):
        raise ValueError(f"Оператор '{filter_expr}' не поддерживается")

    for op in [">", "<", "="]:
        if op in filter_expr:
            parts = filter_expr.split(op)
            if len(parts) != 2:
                raise ValueError(f"Неккоректное выражение фильтра: {filter_expr}")

            column, raw_value = parts[0].strip(), parts[1].strip()
            operator = op
            break
    else:
        raise ValueError(f"Оператор не найден в фильтре: {filter_expr}")

    result = []
    for row in data:
        if column not in row:
            continue
        cell_value = row[column]

        if isinstance(cell_value, (int, float)):
            try:
                filter_value = float(raw_value) if "." in raw_value else int(raw_value)
            except ValueError:
                continue
        else:
            filter_value = raw_value

        if operator == "=" and cell_value == filter_value:
            result.append(row)
        elif operator in [">", "<"]:
            if isinstance(cell_value, (int, float)) and isinstance(
                filter_value, (int, float)
            ):
                if operator == ">" and cell_value > filter_value:
                    result.append(row)
                elif operator == "<" and cell_value < filter_value:
                    result.append(row)

    return result
