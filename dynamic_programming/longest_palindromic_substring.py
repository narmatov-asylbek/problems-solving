
# Index Index String -> Boolean
# Returns if String[Index: Index] is palindrome
def is_palindrome(i, j, s) -> bool:
    while j > i:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

assert is_palindrome(0, 2, "aba") is True
assert is_palindrome(0, 2, "adf") is False
assert is_palindrome(0, 0, "a") is True

# String -> String
# Returns the longest palindromic substring
def longest_palindrome(s: str):
    curr = s[0]
    for i in range(len(s)):
        k = len(s) - 1
        while k > i:
            if k - i + 1 > len(curr) and is_palindrome(i, k, s):
                curr = s[i: k + 1]
            k -= 1
    return curr



print(longest_palindrome('babad'))
print(longest_palindrome('a'))
print(longest_palindrome('cbbd'))

print(longest_palindrome('bb'))
