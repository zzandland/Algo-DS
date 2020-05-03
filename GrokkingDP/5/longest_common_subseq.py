#  Problem Statement #
#  Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

#  A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

#  Example 1:

#  Input: s1 = "abdca"
#  s2 = "cbda"
#  Output: 3
#  Explanation: The longest common subsequence is "bda".

#  Example 2:

#  Input: s1 = "passport"
#  s2 = "ppsspt"
#  Output: 5
#  Explanation: The longest common subsequence is "psspt".

def td(s1: str, s2: str) -> int:
    """
    >>> td('abdca', 'cbda')
    3
    >>> td('passport', 'ppsspt')
    5
    """
    A, B = len(s1), len(s2)
    dp = [[None for _ in range(B)] for _ in range(A)]
    def fn(i: int, j: int) -> int:
        if i == A or j == B: return 0
        if dp[i][j] == None:
            if s1[i] == s2[j]: dp[i][j] = 1 + fn(i+1, j+1)
            else: dp[i][j] = max(fn(i+1, j), fn(i, j+1))
        return dp[i][j]
    return fn(0, 0)

def bu(s1: str, s2: str) -> int:
    """
    >>> bu('abdca', 'cbda')
    3
    >>> bu('passport', 'ppsspt')
    5
    """
    A, B = len(s1), len(s2)
    if B > A: A, B = B, A
    dp = [[0 for _ in range(B+1)] for _ in range(2)]
    for i in range(A):
        for j in range(1, B+1):
            if s1[i] == s2[j-1]: dp[1][j] = dp[0][j-1]+1
            else: dp[1][j] = max(dp[0][j], dp[0][j-1])
        dp[0] = dp[1]
    return dp[1][-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
