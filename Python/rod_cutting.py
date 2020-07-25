   #  0  1  2  3  4  5
#  0  0  1  2  3  4  5
#  1  0  1  3  4  6  7
#  2  0  1  3  4  6  7
#  3  0  1  3  4  6  7

from typing import *

def rod_cutting(N: int, cuts: List[int], prices: List[int]) -> int:
    dp = [0]*(N+1)
    for y, cut in enumerate(cuts):
        for x in range(cut, N+1):
            dp[x] = max(dp[x], prices[y] + dp[x-cut])
    return dp[N]


print(rod_cutting(5, [1,2,3,4],[1,3,2,5]))
def dq(floor: int, egg: int) -> int:
    res = 1 if egg <= 1 else 0
    if floor < 2: return floor
    if floor % 2 == 1:
        return res + dq(floor // 2, egg-1)
    return res + max(dq(floor // 2 - 1, egg-1), dq(floor // 2, egg-1))

print(dq(5, 2))
