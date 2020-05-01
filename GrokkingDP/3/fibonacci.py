def bu(n: int) -> int:
    """
    >>> bu(0)
    0
    >>> bu(5)
    5
    >>> bu(6)
    8
    >>> bu(24)
    46368
    """
    if n < 2: return n
    n1, n2, t = 0, 1, 0
    for i in range(2, n+1):
        n1, n2 = n2, n1+n2
    return n2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
