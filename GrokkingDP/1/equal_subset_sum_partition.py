import typing
List = typing.List

def td(nums: List[int]) -> bool:
    N, s = len(nums), sum(nums)
    if s % 2 == 1: return False
    dp = [[None for _ in range(s//2+1)] for _ in range(N+1)]
    def fn(i: int, r: int) -> bool:
        if i >= N or r < 0: return False
        if r == 0: return True
        if dp[i][r] == None:
            dp[i][r] = fn(i+1, r-nums[i]) or fn(i+1, r)
        return dp[i][r]
    return fn(0, s//2)

def bu(nums: List[int]) -> bool:
    N, s = len(nums), sum(nums)
    if s % 2 == 1: return False
    dp = [[True if i == 0 else False for i in range(s//2+1)] for _ in range(N)]
    for i in range(N):
        for j in range(1, s//2+1):
            if j >= nums[i]: dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
            else: dp[i][j] = dp[i-1][j]
    print("Backtrack: ", backtrack(nums, dp))
    return dp[-1][-1]

def backtrack(nums: List[int], dp: List[List[int]]) -> List[int]:
    y, x, output = len(dp)-1, len(dp[0])-1, []
    print(dp)
    while x > 0 and y > 0:
        if dp[y][x] != dp[y-1][x]:
            output.append(nums[y])
            x -= nums[y]
        y -= 1
    if x != 0: output.append(nums[0])
    return sorted(output)

def buN(nums: List[int]) -> bool:
    N, s = len(nums), sum(nums)
    if s % 2 == 1: return False
    dp = [True if i == 0 else False for i in range(s//2+1)]
    for i in range(N):
        for j in range(s//2, -1, -1):
            dp[j] = dp[j] or dp[j-nums[i] if j >= nums[i] else j]
    return dp[-1]

t1 = [1, 2, 3, 4]
t2 = [1, 1, 3, 4, 7]
t3 = [2, 3, 4, 6]

assert td(t1) == True
assert td(t2) == True
assert td(t3) == False
assert bu(t1) == True
assert bu(t2) == True
assert bu(t3) == False
assert buN(t1) == True
assert buN(t2) == True
assert buN(t3) == False
