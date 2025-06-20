import pytest
from csv_processor.aggregators import apply_aggregation


data = [
    {"name": "iPhone", "price": 999, "rating": 4.9},
    {"name": "Samsung", "price": 1199, "rating": 4.8},
    {"name": "Xiaomi", "price": 299, "rating": 4.4},
]


def test_aggregate_avg():
    result = apply_aggregation(data, "avg:price")
    expected = (999 + 1199 + 299) / 3
    assert result == expected


def test_aggregate_min():
    result = apply_aggregation(data, "min:price")
    assert result == 299


def test_aggregate_max():
    result = apply_aggregation(data, "max:price")
    assert result == 1199


def test_aggregate_invalid_operation():
    with pytest.raises(ValueError):
        apply_aggregation(data, "sum:price")


def test_aggregate_invalid_format():
    with pytest.raises(ValueError):
        apply_aggregation(data, "avg-price")


def test_aggregate_non_numeric_column():
    with pytest.raises(ValueError):
        apply_aggregation(data, "avg:name")


def test_aggregate_column_not_found():
    with pytest.raises(ValueError):
        apply_aggregation(data, "avg:missing_column")
