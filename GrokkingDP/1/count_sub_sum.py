#  Problem Statement #
#  Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

#  Example 1: #
#  Input: {1, 1, 2, 3}, S=4
#  Output: 3

#  The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
#  Note that we have two similar sets {1, 3}, because we have two '1' in our input.

#  Example 2: #
#  Input: {1, 2, 7, 1, 5}, S=9
#  Output: 3

#  The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

import typing
List = typing.List

def bu(nums: List[int], S: int) -> int:
    """
    >>> bu([1, 1, 2, 3], 4)
    3
    >>> bu([1, 2, 7, 1, 5], 9)
    3
    """
    N, dp = len(nums), [1 if i == 0 else 0 for i in range(S+1)]
    for i in range(N):
        for j in range(S, -1, -1):
            if j >= nums[i]: dp[j] += dp[j-nums[i]]
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
