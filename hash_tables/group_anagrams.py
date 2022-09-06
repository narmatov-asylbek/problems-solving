from collections import defaultdict

def group_anagrams(items: list[str]) -> list[str]:
    anagrams = defaultdict(list)

    for item in items:
        anagrams[''.join(sorted(item))].append(item)
    return anagrams.values()