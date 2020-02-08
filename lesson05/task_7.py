import json
result = []
with open('firm.txt') as f:
    firms = 1
    names = []
    profits = []
    for line in f:
        key, value, value1, value2 = line.split()
        names.append(key)
        revenue = int(value1)
        costs = int(value2)
        if revenue > costs:
            profit = revenue - costs
            profits.append(profit)
            firms += 1
            average = sum(profits) / firms
        elif revenue < costs:
            loss = revenue - costs
            profits.append(loss)
average_profit_dict = dict(average_profit=average)
my_list = dict(zip(names, profits))
result.append(my_list)
result.append(average_profit_dict)
print(result)

with open('firm.json', 'w') as f:
    json.dump(result, f)

