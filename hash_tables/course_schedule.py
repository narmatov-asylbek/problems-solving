


# Number [Pair-of Number] -> Boolean
# Can I attend num courses
def can_finish(num, preqs: list[int]) -> bool:
    """
    Num is the num of courses that needs to be attended
    preqs is a pair of (course, prerequesite for course)

    >>> can_finish(2, [[1, 0]])
    True

    >>> can_finish(2, [[1, 0], [0, 1]])
    False 
    """
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()