from typing import List

t1 = ([1,2,3,4,5], [2,6,7,10,13], 5)

def td(lengths: List[int], prices: List[int], L: int) -> int:
    """
    >>> td(*t1)
    14
    """
    N = len(lengths)
    dp = [[0 for _ in range(l+1)] for _ in range(N)]
    def fn(i: int, l: int) -> int:
        if i >= N or w <= 0: return 0
        if not dp[i][l]:
            dp[i][l] = fn(i+1, l) if l < lengths[i] else max(fn(i+1, l), (prices[i]+fn(i, l-lenghts[i])))
        return dp[i][l]

def bu(lengths: List[int], prices: List[int], l: int) -> int:
    """
    >>> bu(*t1)
    14
    """
    N = len(lengths)
    dp = [0 for _ in range(l+1)]
    for i in range(N):
        for j in range(l+1):
            if j >= lengths[i]: dp[j] = max(dp[j], prices[i]+dp[j-lengths[i]])
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
