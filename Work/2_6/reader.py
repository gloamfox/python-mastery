import csv
from sys import intern


def read_csv_as_dicts(filename, coltypes):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        record = []
        for row in rows:
            portfolio = {
                name: func(val) for name, func, val in zip(headers, coltypes, row)
            }
            record.append(portfolio)
        return record


if __name__ == "__main__":
    portfolio = read_csv_as_dicts("Data/portfolio.csv", [str, int, float])
    for s in portfolio:
        print(s)

    rows = read_csv_as_dicts("Data/ctabus.csv", [intern, intern, str, int])
    routeids = {id(row["route"]) for row in rows}
    print(len(routeids))
    print(type(routeids))
