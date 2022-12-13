


def coin_change(coins: list[int], n: int) -> int:
    dp = [0] * (n + 1)

    dp[0] = 1

    for coin in coins:
        for j in range(1, n + 1):
            if coin > j:
                continue
            dp[j] += dp[j - coin]
    return dp[n] if dp[n] != n + 1 else -1



print(coin_change([2, 3, 5, 6], 10))