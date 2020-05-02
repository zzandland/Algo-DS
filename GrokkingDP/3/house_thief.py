#  There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses. The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system. How should the thief maximize his stealing?

#  Problem Statement #
#  Given a number array representing the wealth of ‘n’ houses, determine the maximum amount of money the thief can steal without alerting the security system.

#  Example 1:

#  Input: {2, 5, 1, 3, 6, 2, 4}
#  Output: 15
#  Explanation: The thief should steal from houses 5 + 6 + 4

#  Example 2:

#  Input: {2, 10, 14, 8, 1}
#  Output: 18
#  Explanation: The thief should steal from houses 10 + 8

from typing import List

def td(wealths: List[int]) -> int:
    """
    >>> td([2,5,1,3,6,2,4])
    15
    >>> td([2,10,14,8,1])
    18
    """
    N = len(wealths)
    dp = [0]*N
    def fn(i: int) -> int:
        if i >= N: return 0
        if not dp[i]: dp[i] = max(wealths[i] + fn(i+2), fn(i+1))
        return dp[i]
    return fn(0)

def bu(wealths: List[int]) -> int:
    """
    >>> bu([2,5,1,3,6,2,4])
    15
    >>> bu([2,10,14,8,1])
    18
    """
    n = len(wealths)
    if n == 0: return 0
    n1, n2 = 0, wealths[0]
    for i in range(1, n):
        n1, n2 = n2, max(wealths[i]+n1, n2)
    return n2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
