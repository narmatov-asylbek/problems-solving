

def coin_change(coins: list[int], amount: int) -> int:
    table = [amount + 1] * (amount + 1)
    table[0] = 0

    for coin in coins:
        for j in range(1, len(table)):
            if coin > j:
                continue
            curr = 1 + table[j - coin]
            table[j] = min(curr, table[j])
    return table[amount] if table[amount] != amount + 1 else -1


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))
print(coin_change([7, 8, 9, 10, 11], 13))
