import pytest
from csv_processor import apply_filter

data = [
    {"name": "iPhone", "brand": "apple", "price": 999, "rating": 4.9},
    {"name": "Samsung", "brand": "samsung", "price": 1199, "rating": 4.8},
    {"name": "Xiaomi", "brand": "xiaomi", "price": 299, "rating": 4.4},
]


def test_filter_greater_than():
    result = apply_filter(data, "price>500")
    assert len(result) == 2
    assert all(row["price"] > 500 for row in result)


def test_filter_less_than():
    result = apply_filter(data, "price<500")
    assert len(result) == 1
    assert result[0]["name"] == "Xiaomi"


def test_filter_equals_text():
    result = apply_filter(data, "brand=apple")
    assert len(result) == 1
    assert result[0]["name"] == "iPhone"


def test_filter_equals_number():
    result = apply_filter(data, "price=1199")
    assert len(result) == 1
    assert result[0]["brand"] == "samsung"


def test_filter_invalid_operator():
    with pytest.raises(ValueError):
        apply_filter(data, "price!=999")


def test_filter_non_existing_column():
    result = apply_filter(data, "nonexistent=123")
    assert result == []