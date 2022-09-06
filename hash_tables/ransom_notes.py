from collections import defaultdict

def can_construct(notes: str, magazine: str) -> bool:
    letters = defaultdict(lambda: 0)
    for letter in magazine:
        letters[letter] += 1
    

    for letter in notes:
        letters[letter] -= 1
        if letters[letter] < 0:
            return False
    return True