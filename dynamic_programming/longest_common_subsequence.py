


def lcs(t1: str, t2: str) -> int:
    dp = [0] * len(t1)
    curr_max = 0

    for s in t2:
        for i, v in enumerate(t1):
            if s == v:
                dp[i] = max(dp[i] + 1, dp[i - 1])
                curr_max = max(dp[i], curr_max)
    return curr_max


print(lcs("abcde", "ace"))
print(lcs("abc", "abc"))
print(lcs("abc", "def"))