#  Problem Statement #
#  Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. We can assume an infinite supply of item quantities; therefore, each item can be selected multiple times.

from typing import List

t1 = ([1, 2, 3,], [15, 20, 50], 5)
t2 = ([1, 3, 4, 5], [15, 50, 60, 90], 8)
t3 = ([1, 3, 4, 5], [15, 50, 60, 90], 6)

def td(weights: List[int], profits: List[int], C: int) -> int:
    """
    >>> td(*t1)
    80
    >>> td(*t2)
    140
    >>> td(*t3)
    105
    """
    N = len(weights)
    dp = [[0 for _ in range(C+1)] for _ in range(N)]
    def fn(i: int, c: int) -> int:
        if c <= 0 or i >= N: return 0
        if not dp[i][c]:
            if c >= weights[i]: dp[i][c] = max(fn(i+1, c), (profits[i] + fn(i, c-weights[i])))
            else: dp[i][c] = fn(i+1, c)
        return dp[i][c]
    return fn(0, C)

def bu(weights: List[int], profits: List[int], C: int) -> int:
    """
    >>> bu(*t1)
    80
    >>> bu(*t2)
    140
    >>> bu(*t3)
    105
    """
    N = len(weights)
    dp = [0 for _ in range(C+1)]
    for i in range(N):
        for j in range(1, C+1):
            if j >= weights[i]: dp[j] = max(dp[j], profits[i] + dp[j-weights[i]])
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
