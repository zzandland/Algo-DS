#  Problem Statement #
#  Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters. Write a function to calculate the count of the minimum number of edit operations.

#  Example 1:

#  Input: s1 = "bat"
#  s2 = "but"
#  Output: 1
#  Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.

#  Example 2:

#  Input: s1 = "abdca"
#  s2 = "cbda"
#  Output: 2
#  Explanation: We can replace first 'a' with 'c' and delete second 'c'.

#  Example 3:

#  Input: s1 = "passpot"
#  s2 = "ppsspqrt"
#  Output: 3
#  Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.

t1 = ('bat', 'but')
t2 = ('abdca', 'cbda')
t3 = ('passpot', 'ppsspqrt')

def td(s1: str, s2: str) -> int:
    """
    >>> td(*t1)
    1
    >>> td(*t2)
    2
    >>> td(*t3)
    3
    """
    A, B = len(s1), len(s2)
    dp = [[None]*B for _ in range(A)]
    def fn(i: int, j: int) -> int:
        if i == A and j == B: return 0
        if i == A or j == B: return float('inf')
        if dp[i][j] is None:
            if s1[i] == s2[j]: dp[i][j] = fn(i+1, j+1)
            else: dp[i][j] = 1 + min(fn(i+1, j+1), fn(i+1, j), fn(i, j+1))
        return dp[i][j]
    return fn(0, 0)

def bu(s1: str, s2: str) -> int:
    """
    >>> bu(*t1)
    1
    >>> bu(*t2)
    2
    >>> bu(*t3)
    3
    """
    A, B = len(s1), len(s2)
    if B > A: A, B, s1, s2 = B, A, s2, s1
    dp, cnt = [[0]*B for _ in range(2)], 0
    yv = xv = False
    for a in range(B):
        if s2[a] == s1[0] and not xv: xv = True
        else: cnt += 1
        dp[0][a] = cnt
    for i in range(1, A):
        for j in range(B):
            if j == 0:
                if s1[i] == s2[j] and not yv: yv = True
                else: dp[1][j] = dp[0][j] + 1
            else:
                if s1[i] == s2[j]: dp[1][j] = dp[0][j-1]
                else: dp[1][j] = 1 + min(dp[0][j], dp[1][j-1], dp[0][j-1])
        dp[0] = dp[1][:]
    return dp[1][-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
