class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = ['0'] if N == 1 else []
        if K == 0:
            for i in range(1, 10):
                res.append(int(str(i)*N))
            return res
        def dfs(num: str) -> List[int]:
            if len(num) == N: return [int(num)]
            res = []
            up, down = int(num[-1]) + K, int(num[-1]) - K
            if 0 <= down < 10: res += dfs(num + str(down))
            if 0 <= up < 10: res += dfs(num + str(up))
            return res
        for i in range(1, 10):
            res += dfs(str(i))
        return res