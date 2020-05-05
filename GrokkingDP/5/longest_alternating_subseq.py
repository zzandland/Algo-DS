#  Problem Statement #
#  Given a number sequence, find the length of its Longest Alternating Subsequence (LAS). A subsequence is considered alternating if its elements are in alternating order.

#  A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:

#  {a1 > a2 < a3 } or { a1 < a2 > a3}.
#  Example 1:

#  Input: {1,2,3,4}
#  Output: 2
#  Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}
#  Example 2:

#  Input: {3,2,1,4}
#  Output: 3
#  Explanation: The LAS are {3,2,4} and {2,1,4}.
#  Example 3:

#  Input: {1,3,2,4}
#  Output: 4
#  Explanation: The LAS is {1,3,2,4}. }

from typing import List

t1 = [1,2,3,4]
t2 = [3,2,1,4]
t3 = [1,3,2,4]

def td(nums: List[int]) -> int:
    """
    >>> td(t1)
    2
    >>> td(t2)
    3
    >>> td(t3)
    4
    """
    N = len(nums)
    dp = [[[None] * N for _1 in range(N)] for _2 in range(2)]
    def fn(i: int, j: int, asc: int) -> int:
        if i == N: return 1
        if j > i: return 0
        if dp[asc][i][j] == None:
            if asc:
                dp[asc][i][j] = 1 + fn(i+1, i, 0) if nums[i] > nums[j] else max(fn(i, j+1, 1), fn(i+1, j, 1))
            else:
                dp[asc][i][j] = 1 + fn(i+1, i, 1) if nums[i] < nums[j] else max(fn(i, j+1, 0), fn(i+1, j, 0))
        return dp[asc][i][j]
    return max(fn(0, 0, 1), fn(0, 0, 0))
def bu(nums: List[int]) -> int:
    """
    >>> bu(t1)
    2
    >>> bu(t2)
    3
    >>> bu(t3)
    4
    """
    N = len(nums)
    dp = [[1] * N for _ in range(2)]
    for i in range(N):
        for asc in range(2):
            for j in range(i):
                if not asc and nums[i] < nums[j] and dp[0][i] <= dp[1][j]: dp[0][i] = dp[1][j] + 1
                if nums[i] > nums[j] and dp[1][i] <= dp[0][j]: dp[1][i] = dp[0][j] + 1
    return max(dp[0][-1], dp[1][-1])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
