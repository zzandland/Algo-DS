import typing
List = typing.List

def td(weights: List[int], profits: List[int], capacity: int) -> int:
    N = len(weights)
    dp = [[0 for _ in range(capacity+1)] for _ in range(N+1)]
    def fn(i: int, curW: int, curP: int) -> int:
        if curW < 0: return 0
        if i >= N or curW == 0: return curP
        if not dp[i][curW]:
            dp[i][curW] = max(fn(i+1, curW-weights[i], curP+profits[i]), fn(i+1, curW, curP))
        return dp[i][curW]
    return fn(-1, capacity, 0)

def bu(weights: List[int], profits: List[int], capacity: int) -> int:
    N = len(weights)
    dp = [[0 for _ in range(capacity+1)] for _ in range(N)]
    for i in range(N):
        for j in range(capacity, -1, -1):
            if j >= weights[i]: dp[i][j] = max(profits[i]+dp[i-1][j-weights[i]], dp[i][j])
            else: dp[i][j] = dp[i-1][j]
    print("Backtrack: ", backtrack(weights, profits, dp))
    return dp[-1][-1]

def buN(weights: List[int], profits: List[int], capacity: int) -> int:
    N = len(weights)
    dp = [0 for _ in range(capacity+1)]
    for i in range(N):
        for j in range(capacity, -1, -1):
            if j >= weights[i]: dp[j] = max(profits[i]+dp[j-weights[i]], dp[j])
            else: dp[j] = dp[j]
    return dp[-1]

def backtrack(weights: List[int], profits: List[int], dp: List[List[int]]) -> List[int]:
    y, x, output = len(dp)-1, len(dp[0])-1, []
    while x > 0:
        if dp[y][x] != dp[y-1][x]:
            output.append(y)
            x -= weights[y]
        y -= 1
    return output[::-1]

weights = [1, 2, 3, 5]
profits = [1, 6, 10, 16]
capacity = 7

print(bu(weights, profits, capacity))
