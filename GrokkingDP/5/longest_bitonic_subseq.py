#  Problem Statement #
#  Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

#  Example 1:

#  Input: {4,2,3,6,10,1,12}
#  Output: 5
#  Explanation: The LBS is {2,3,6,10,1}.

#  Example 2:

#  Input: {4,2,5,9,7,6,10,3,1}
#  Output: 7
#  Explanation: The LBS is {4,5,9,7,6,3,1}.

from typing import List

t1 = [4,2,3,6,10,1,12]
t2 = [4,2,5,9,7,6,10,3,1]

def td(nums: List[int]) -> int:
    """
    >>> td(t1)
    5
    >>> td(t2)
    7
    """
    N = len(nums)
    dp = [[[None] * N for _ in range(N)] for _ in range(2)]
    def fn(i: int, j: int, asc: int) -> int:
        if i == N: return 1
        if i < j: return 0
        if dp[asc][i][j] == None:
            if asc:
                if nums[i] > nums[j]: dp[asc][i][j] = 1 + max(fn(i+1, j+1, 1), fn(i+1, j+1, 0))
                else: dp[asc][i][j] = max(fn(i+1, j, 1), fn(i, j+1, 1), fn(i+1, j, 0), fn(i, j+1, 0))
            else:
                if nums[i] < nums[j]: dp[asc][i][j] = 1 + fn(i+1, j+1, 0)
                else: dp[asc][i][j] = max(fn(i+1, j, 0), fn(i, j+1, 0))
        return dp[asc][i][j]
    return fn(0, 0, 1)

def bu(nums: List[int]) -> int:
    """
    >>> bu(t1)
    5
    >>> bu(t2)
    7
    """
    N = len(nums)
    dp = [[1]*N for _ in range(2)]
    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if nums[i] > nums[j] and dp[0][i] <= dp[0][j]: dp[0][i] += 1
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j] and dp[1][i] <= dp[1][j]: dp[1][i] += 1
    return max([dp[1][i] + dp[0][i+1] for i in range(N-1)])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
