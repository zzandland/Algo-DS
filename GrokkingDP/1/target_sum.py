#  Problem Statement #
#  Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

#  Example 1: #
#  Input: {1, 1, 2, 3}, S=1
#  Output: 3
#  Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

#  Example 2: #
#  Input: {1, 2, 7, 1}, S=9
#  Output: 2
#  Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
import typing
List = typing.List

t1 = ([1, 1, 2, 3], 1)
t2 = ([1, 2, 7, 1], 9)

def td(nums: List[int], S: int) -> int:
    """
    >>> td(*t1)
    3
    >>> td(*t2)
    2
    """
    N = len(nums)
    dp = {}
    def fn(i: int, s: int) -> int:
        if i >= N: return 1 if s == 0 else 0
        key = '{}:{}'.format(i, s)
        if key not in dp: dp[key] = fn(i+1, s+nums[i]) + fn(i+1, s-nums[i])
        return dp[key]
    return fn(0, S)

def bu(nums: List[int], S: int) -> int:
    """
    >>> bu(*t1)
    3
    >>> bu(*t2)
    2
    """
    N, s = len(nums), (sum(nums)+S)//2
    if s % 2 == 1: return 0
    dp = [1 if i == 0 else 0 for i in range(s+1)]
    for i in range(N):
        for j in range(s, -1, -1):
            if j >= nums[i]: dp[j] += dp[j-nums[i]]
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
