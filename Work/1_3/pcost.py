
cost = 0.0
with open('Data/portfolio.dat') as f:

    rows = f.readlines()
    for row in rows:
        raw = row.split()
        cost += int(raw[1]) * float(raw[2])

print("cost:", cost)