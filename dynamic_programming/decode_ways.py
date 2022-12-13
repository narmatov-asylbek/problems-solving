
MAPPER = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    '10': 'J',
    '11': 'K',
    '12': 'L',
    '13': 'M',
    '14': 'N',
    '15': 'O',
    '16': 'P',
    '17': 'Q',
    '18': 'R',
    '19': 'S',
    '20': 'T',
    '21': 'U',
    '22': 'V',
    '23': 'W',
    '24': 'X',
    '25': 'Y',
    '26': 'Z'
}

# Int-strings -> int
# Returns a number of possible ways to decode the string s
def num_decodings(s: str) -> int:
    """
    >>> num_decodings('12')
    2
    
    >>> num_decodings('226')
    3
    
    >>> num_decodings('06')
    0
    """
    
    def helper(i: int) -> int:
        if i >= len(s):
            return 0
        w = s[i:]
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()