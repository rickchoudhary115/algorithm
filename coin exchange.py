def coin_brute(coins, amount):

    if amount == 0:
        return 0

    ans = float('inf')

    for coin in coins:

        if coin <= amount:
            ans = min(ans, 1 + coin_brute(coins, amount - coin))

    return ans
def coin_dp(coins, amount):

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount]

def coin_greedy(coins, amount):

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count

coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

print("Minimum Coins using Dynamic Programming =", coin_dp(coins, amount))
print("Minimum Coins using Brute Force =", coin_brute(coins, amount))
print("Minimum Coins using Greedy =", coin_greedy(coins, amount))