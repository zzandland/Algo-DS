#  Problem Statement #
#  Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

#  Example 1:

#  Input: {4,1,2,6,10,1,12}
#  Output: 32
#  Explanation: The increaseing sequence is {4,6,10,12}.
#  Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.

#  Example 2:

#  Input: {-4,10,3,7,15}
#  Output: 25
#  Explanation: The increaseing sequences are {10, 15} and {3,7,15}.

from typing import List

def td(nums: List[int]) -> int:
    """
    >>> td([4,1,2,6,10,1,12])
    32
    >>> td([-4,10,3,7,15])
    25
    """
    N = len(nums)
    dp = [[0 for _ in range(N+1)] for _ in range(N)]
    def fn(i: int, j: int) -> int:
        if i == N: return 0
        if j == -1 or nums[i] > nums[j]: dp[i][j+1] = nums[i] + fn(i+1, i)
        dp[i][j+1] = max(fn(i+1, j), dp[i][j+1])
        return dp[i][j+1]
    return fn(0, -1)

def bu(nums: List[int]) -> int:
    """
    >>> bu([4,1,2,6,10,1,12])
    32
    >>> bu([-4,10,3,7,15])
    25
    """
    N, mx = len(nums), 0
    dp = nums[:]
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j]: dp[i] = max(dp[i], nums[i] + dp[j])
        mx = max(mx, dp[i])
    return mx

if __name__ == '__main__':
    import doctest
    doctest.testmod()
