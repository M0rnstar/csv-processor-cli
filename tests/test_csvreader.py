from csv_processor.csv_reader import read_csv

def test_read_csv_text(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,brand\niphone,apple")

    result = read_csv(str(csv_file))
    assert result == [{"name": "iphone", "brand": "apple"}]
    assert all(isinstance(value, str) for row in result for value in row.values())
