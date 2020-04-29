#  Problem Statement #
#  Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

#  Example 1: #
#  Input: {1, 2, 3, 9}
#  Output: 3

#  Explanation: We can partition the given set into two subsets where minimum absolute difference
#  between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

#  Example 2: #
#  Input: {1, 2, 7, 1, 5}
#  Output: 0

#  Explanation: We can partition the given set into two subsets where minimum absolute difference
#  between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

#  Example 3: #
#  Input: {1, 3, 100, 4}
#  Output: 92

#  Explanation: We can partition the given set into two subsets where minimum absolute difference
#  between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

import typing
List = typing.List
t1 = [1, 2, 3, 9]
t2 = [1, 2, 7, 1, 5]
t3 = [1, 3, 100, 4]

def td(nums: List[int]) -> int:
    """
    >>> td(t1)
    3
    >>> td(t2)
    0
    >>> td(t3)
    92
    """
    N, S = len(nums), sum(nums)
    dp = {}
    def fn(i: int, cur: int) -> int:
        if i >= N: return abs((S-cur) - cur)
        key = str(i)+':'+str(cur)
        if key not in dp: dp[key] = min(fn(i+1, cur+nums[i]), fn(i+1, cur))
        return dp[key]
    return fn(0, 0)

def bu(nums: List[int]) -> int:
    """
    >>> bu(t1)
    3
    >>> bu(t2)
    0
    >>> bu(t3)
    92
    """
    N, S = len(nums), sum(nums)
    dp, mx = [True if i == 0 else False for i in range(S//2+1)], 0
    for i in range(N):
        for j in range(S//2, -1, -1):
            if j >= nums[i]: dp[j] = dp[j] or dp[j-nums[i]]
            if dp[j]: mx = max(mx, j)
    return abs((S-mx)-mx)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
