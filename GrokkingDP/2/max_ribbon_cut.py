#  Introduction #
#  We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. Now we need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

#  Example 1:
#  n: 5
#  Ribbon Lengths: {2,3,5}
#  Output: 2
#  Explanation: Ribbon pieces will be {2,3}.

#  Example 2:
#  n: 7
#  Ribbon Lengths: {2,3}
#  Output: 3
#  Explanation: Ribbon pieces will be {2,2,3}.

#  Example 3:
#  n: 13
#  Ribbon Lengths: {3,5,7}
#  Output: 3
#  Explanation: Ribbon pieces will be {3,3,7}.

#  Problem Statement #
#  Given a number array to represent possible ribbon lengths and a total ribbon length ‘n’, we need to find the maximum number of pieces that the ribbon can be cut into.

from typing import List

t1 = ([2,3,5], 5)
t2 = ([2,3], 7)
t3 = ([3,5,7], 13)

def td(lengths: List[int], L: int) -> int:
    """
    >>> td(*t1)
    2
    >>> td(*t2)
    3
    >>> td(*t3)
    3
    """
    N = len(lengths)
    dp = [[None for _ in range(L+1)] for _ in range(N)]
    def fn(i: int, l: int, c: int) -> int:
        if l == 0: return c
        if i >= N or l < 0: return 0
        if dp[i][l] == None: dp[i][l] = max(fn(i, l-lengths[i], c+1), fn(i+1, l, c))
        return dp[i][l]
    return fn(0, L, 0)

def bu(lengths: List[int], L: int) -> int:
    """
    >>> bu(*t1)
    2
    >>> bu(*t2)
    3
    >>> bu(*t3)
    3
    """
    N = len(lengths)
    dp = [0] + [-1]*L
    for l in lengths:
        for j in range(l, L+1):
            dp[j] = max(dp[j], dp[j-l]+1 if dp[j-l] != -1 else -1)
    return dp[-1]

if __name__ == '__main__':
    from doctest import testmod
    testmod()
