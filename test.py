import pytest
from script import read_csv_file, calculate_payout, generate_report
def test_read_csv_file():
    file_path = 'test.csv'
    data = read_csv_file(file_path)
    assert len(data) == 3
def test_calculate_payout():
    data = [
        {'hourly_rate': '50', 'hours_worked': '160'},
        {'hourly_rate': '40', 'hours_worked': '150'},
        {'hourly_rate': '60', 'hours_worked': '170'}
    ]
    payout = calculate_payout(data)
    assert payout == 24800
def test_generate_report():
    data = [
        {'hourly_rate': '50', 'hours_worked': '160'},
        {'hourly_rate': '40', 'hours_worked': '150'},
        {'hourly_rate': '60', 'hours_worked': '170'}
    ]
    report = generate_report(data, 'payout')
    assert report == 'Общая зарплата: 24800'