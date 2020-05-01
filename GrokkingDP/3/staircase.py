def bu(n: int) -> int:
    """
    >>> bu(0)
    1
    >>> bu(3)
    4
    >>> bu(4)
    7
    """
    if n < 2: return 1
    if n == 2: return 2
    n1, n2, n3 = 1, 1, 2
    for i in range(3, n+1):
        n1, n2, n3 = n2, n3, n1+n2+n3
    return n3

if __name__ == '__main__':
    import doctest
    doctest.testmod()
