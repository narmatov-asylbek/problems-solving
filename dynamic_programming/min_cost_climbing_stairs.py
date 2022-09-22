


def min_cost(cost: list[int]) -> int:
    
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]
    

    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    
    return min(dp[-1], dp[-2])

print(min_cost([10,15,20]))
print(min_cost([1,100,1,1,1,100,1,1,100,1]))

