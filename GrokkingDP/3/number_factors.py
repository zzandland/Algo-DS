def bu(n: int) -> int:
    """
    >>> bu(0)
    1
    >>> bu(4)
    4
    >>> bu(5)
    6
    """
    if n < 3: return 1
    if n == 3: return 2
    n1, n2, n3, n4 = 1, 1, 1, 2
    for i in range(4, n+1):
        n1, n2, n3, n4 = n2, n3, n4, n1+n2+n4
    return n4

if __name__ == '__main__':
    import doctest
    doctest.testmod()
