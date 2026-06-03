from itertools import permutations

n = int(input("Enter number of cities: "))

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

cities = range(1, n)

min_cost = float('inf')

for path in permutations(cities):

    cost = graph[0][path[0]]

    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]

    cost += graph[path[-1]][0]

    min_cost = min(min_cost, cost)

print("Minimum Cost =", min_cost)