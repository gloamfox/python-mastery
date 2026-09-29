import csv


def csv_as_dicts(lines, types, *, headers=None):

    return convert_csv(
        lines,
        lambda headers, row: {
            name: func(val) for name, func, val in zip(headers, types, row)
        },
    )


def csv_as_instances(lines, cls, *, headers=None):
    return convert_csv(lines, lambda headers, row: cls.from_row(row))


def read_csv_as_dicts(filename, types, *, headers=None):
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)


def read_csv_as_instances(filename, cls, *, headers=None):
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)


def convert_csv(lines, converter, *, headers=None):
    # records = []
    # rows = csv.reader(lines)
    # if headers is None:
    #     headers = next(rows)
    # for row in rows:
    #     record = converter(headers, row)
    #     records.append(record)
    # return records

    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    return list(map(lambda row: converter(headers, row), rows))
