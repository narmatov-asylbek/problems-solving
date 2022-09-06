from collections import defaultdict


def palindromic_permutation(string: str) -> bool:
    counter = defaultdict(lambda: 0)

    for s in string:
        counter[s] += 1
    

    can_have_one = len(string) % 2 != 0
    for c in counter.values():
        if c % 2 != 0:
            if can_have_one:
                can_have_one = False
                continue
            return False
    return True
