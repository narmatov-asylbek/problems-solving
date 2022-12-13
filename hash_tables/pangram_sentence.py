

def check_pangram(sentence: str) -> bool:
    return len({x for x in sentence}) == 26