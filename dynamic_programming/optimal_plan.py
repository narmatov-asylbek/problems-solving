

# List[int]  List[int] int -> int
# Returns maximum profit of given available
# Constraints:
#   - len(prices) == len(profits)
#   - aval >= 1
def max_profit(prices: list[int], profits: list[int], aval: int) -> int:
    dp = [0] * (aval + 1)
    dp[0] = 0

    for i in range(len(prices)):
        for j in range(1, aval + 1):
            if prices[i] > j:
                continue
            print(dp)
            dp[j] = max(profits[i] + dp[j - prices[i]], dp[j])
    print(dp)
    return dp[-1]

print(max_profit([1, 2, 3], [2, 3, 5], 7))