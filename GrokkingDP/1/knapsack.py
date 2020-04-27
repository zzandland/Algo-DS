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
    N= len(weights)
    dp = [[0 for _ in range(capacity+1)] for _ in range(N)]
    for i in range(N):
        for j in range(capacity+1):
            if j >= weights[i]: dp[i][j] = max(profits[i]+dp[i-1][j-weights[i]], dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

weights = [ 2, 3, 1, 4 ]
profits = [ 4, 5, 3, 7 ]
capacity = 5

print(bu(weights, profits, capacity))
