import csv
from typing import List


def read_csv_as_dicts(filename, types):
    with open(filename) as f:
        return csv_as_dicts(f, types)


def read_csv_as_instances(filename, cls):
    with open(filename) as file:
        return csv_as_instances(file, cls)


def csv_as_dicts(file, types):
    records = []
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(file, cls):
    records = []
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


def add(x:int, y:int) -> int:
    return x+y

def sum_squares(nums:List[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total


if __name__ == "__main__":

    from stock import Stock

    port = read_csv_as_dicts("Data/portfolio.csv", [str, int, float])
    print(port)

    port = read_csv_as_instances("Data/portfolio.csv", Stock)
    print(port)

    import gzip

    file = gzip.open('Data/portfolio.csv.gz', 'rt')
    port = csv_as_dicts(file, [str, int, float])
    print(port)

    ...
