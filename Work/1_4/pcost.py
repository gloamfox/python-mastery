

def portfolio_cost(file_name):
    with open(file_name) as f:
        lines = f.readlines()

        cost = 0.0
        for line in lines:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                cost += nshares * price
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)
        return cost

print(portfolio_cost("Data/portfolio3.dat"))