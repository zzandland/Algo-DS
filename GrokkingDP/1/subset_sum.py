import typing

List = typing.List

t1 = ([1, 2, 3, 7], 6)
t2 = ([1, 2, 7, 1, 5], 10)
t3 = ([1, 3, 4, 8], 6)

def td(nums: List[int], target: int) -> bool:
    """
    >>> td(*t1)
    True
    >>> td(*t2)
    True
    >>> td(*t3)
    False
    """
    N = len(nums)
    dp = [[None for _ in range(target+1)] for _ in range(N)]
    def fn(i: int, s: int) -> bool:
        if i >= N or s < 0: return False
        if s == 0: return True
        if dp[i][s] == None: dp[i][s] = fn(i+1, s-nums[i]) or fn(i+1, s)
        return dp[i][s]
    return fn(0, target)

def bu(nums: List[int], target:int) -> bool:
    """
    >>> td(*t1)
    True
    >>> td(*t2)
    True
    >>> td(*t3)
    False
    """
    N = len(nums)
    dp = [None for _ in range(target+1)]
    for i in range(N):
        for j in range(target, -1, -1):
            if j >= nums[i]: dp[j] = dp[j] or dp[j-nums[i]]
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
