def subset_sum_brute(arr, target):

    n = len(arr)

    for mask in range(1 << n):

        total = 0

        for i in range(n):

            if mask & (1 << i):
                total += arr[i]

        if total == target:
            return True

    return False

def subset_sum_dp(arr, target):

    n = len(arr)

    dp = [[False] * (target + 1)
          for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):

        for j in range(1, target + 1):

            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or \
                           dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))

print(subset_sum_dp(arr, target))
print(subset_sum_brute(arr, target))