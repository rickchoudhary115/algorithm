def fractional_knapsack(weights, values, capacity):

    items = []

    for i in range(len(weights)):
        items.append((values[i] / weights[i], weights[i], values[i]))

    items.sort(reverse=True)

    profit = 0

    for ratio, weight, value in items:

        if capacity >= weight:
            profit += value
            capacity -= weight

        else:
            profit += ratio * capacity
            break

    return profit


n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter capacity: "))

print("Maximum Profit =", fractional_knapsack(weights, values, capacity))