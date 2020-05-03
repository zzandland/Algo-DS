#  Problem Statement #
#  Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. Write a function to calculate the count of the minimum number of deletion and insertion operations.

#  Example 1:

#  Input: s1 = "abc"
#  s2 = "fbc"
#  Output: 1 deletion and 1 insertion.
#  Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.

#  Example 2:

#  Input: s1 = "abdca"
#  s2 = "cbda"
#  Output: 2 deletions and 1 insertion.
#  Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

#  Example 3:

#  Input: s1 = "passport"
#  s2 = "ppsspt"
#  Output: 3 deletions and 1 insertion
#  Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.
from typing import Tuple

def bu(s1: str, s2: str) -> Tuple[int, int]:
    """
    >>> bu('abc', 'fbc')
    (1, 1)
    >>> bu('abdca', 'cbda')
    (2, 1)
    >>> bu('passport', 'ppsspt')
    (3, 1)
    """
    A, B = len(s1), len(s2)
    if B > A: A, B = B, A
    dp = [[0 for _ in range(B+1)] for _ in range(2)]
    for i in range(A):
        for j in range(1, B+1):
            if s1[i] == s2[j-1]: dp[1][j] = dp[0][j-1] + 1
            else: dp[1][j] = max(dp[0][j], dp[1][j-1])
        dp[0] = dp[1]
    return (A-dp[1][-1], B-dp[1][-1])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
