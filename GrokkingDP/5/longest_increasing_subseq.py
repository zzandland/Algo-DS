#  Problem Statement #
#  Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

#  Example 1:

#  Input: {4,2,3,6,10,1,12}
#  Output: 5
#  Explanation: The LIS is {2,3,6,10,12}.

#  Example 2:

#  Input: {-4,10,3,7,15}
#  Output: 4
#  Explanation: The LIS is {-4,3,7,15}.

from typing import List

def td(nums: List[int]) -> int:
    """
    >>> td([4,2,3,6,10,1,12])
    5
    >>> td([-4,10,3,7,15])
    4
    >>> td([5,4,3,2,1,2,3,5])
    4
    """
    N = len(nums)
    dp = [[0 for _ in range(N+1)] for _ in range(N)]
    def fn(i: int, prev: int) -> int:
        if i == N: return 0
        if prev == -1 or nums[prev] < nums[i]: dp[i][prev+1] = 1 + fn(i+1, i)
        dp[i][prev+1] = max(dp[i][prev+1], fn(i+1, prev))
        return dp[i][prev+1]
    return fn(0, -1)

def bu(nums: List[int]) -> int:
    """
    >>> bu([4,2,3,6,10,1,12])
    5
    >>> bu([-4,10,3,7,15])
    4
    >>> bu([5,4,3,2,1,2,3,5])
    4
    """
    if not nums: return 0
    N, mx = len(nums), 1
    dp = [1 for i in range(N)]
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]: dp[i] += 1
            mx = max(mx, dp[i])
    return mx

if __name__ == '__main__':
    import doctest
    doctest.testmod()
