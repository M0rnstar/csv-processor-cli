from csv_processor.parser import parse_args
import sys

def test_parse_args(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['main.py', '--file', 'test.csv', '--filter', 'price>100'])
    args = parse_args()
    assert args.file == 'test.csv'
    assert args.filter == 'price>100'
    assert args.aggregate is None
