def knapsack_brute(weights, values, capacity):
    n = len(weights)
    max_profit = 0

    for mask in range(1 << n):
        total_w = 0
        total_v = 0

        for i in range(n):
            if mask & (1 << i):
                total_w += weights[i]
                total_v += values[i]

        if total_w <= capacity:
            max_profit = max(max_profit, total_v)

    return max_profit


def knapsack_dp(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input Section
n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter knapsack capacity: "))

# Output
print("\nBrute Force Answer =", knapsack_brute(weights, values, capacity))
print("Dynamic Programming Answer =", knapsack_dp(weights, values, capacity))