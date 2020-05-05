#  Problem Statement #
#  Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

t1 = ('baxmx', 'ax')
t2 = ('tomorrow', 'tor')
t3 = ('tomorrow', 'torw')

def td(s: str, p: str) -> int:
    """
    >>> td(*t1)
    2
    >>> td(*t2)
    4
    >>> td(*t3)
    4
    """
    S, P = len(s), len(p)
    dp = [[None]*P for _ in range(S)]
    def fn(i: int, j: int) -> int:
        if j == P: return 1
        if i == S: return 0
        if dp[i][j] == None:
            if s[i] == p[j]: dp[i][j] = fn(i+1, j+1) + fn(i+1, j)
            else: dp[i][j] = fn(i+1, j)
        return dp[i][j]
    return fn(0, 0)

def bu(s: str, p: str) -> int:
    """
    >>> bu(*t1)
    2
    >>> bu(*t2)
    4
    >>> td(*t3)
    4
    """
    S, P = len(s), len(p)
    dp = [[1]*(S+1), [0]*(S+1)]
    for i in range(P):
        for j in range(S):
            if p[i] == s[j]: dp[1][j+1] = dp[0][j+1] + dp[1][j]
            else: dp[1][j+1] = dp[1][j]
        dp[0] = dp[1][:]
    return dp[1][-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
