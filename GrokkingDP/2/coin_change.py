from typing import List

t1 = ([1,2,3], 5)
t2 = ([2, 3, 5, 10, 15], 183)

def td(denoms: List[int], target: int) -> int:
    """
    >>> td(*t1)
    5
    >>> td(*t2)
    0
    """
    N = len(denoms)
    dp = [[None for _ in range(target+1)] for _ in range(N)]
    def fn(i: int, c: int) -> int:
        if c == 0: return 1
        if i >= N or c < 0: return 0
        if dp[i][c] == None: dp[i][c] = fn(i, c-denoms[i]) + fn(i+1, c)
        return dp[i][c]
    return fn(0, target)

def bu(denoms: List[int], target: int) -> int:
    """
    >>> bu(*t1)
    5
    >>> bu(*t2)
    0
    """
    N = len(denoms)
    dp = [1 if i % denoms[0] == 0 else 0 for i in range(target+1)]
    for i in range(1, N):
        for j in range(1, target+1):
            if j >= denoms[i]: dp[j] += dp[j-denoms[i]]
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
