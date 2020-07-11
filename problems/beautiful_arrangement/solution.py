class Solution:
    def countArrangement(self, N: int) -> int:
        valids = [set() for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i % j == 0 or j % i == 0:
                    valids[i].add(j)
                    valids[j].add(i)
                    
        def dfs(i: int, seen: set) -> int:
            if i == N: return 1
            left = valids[i+1] - seen
            if not left: return 0
            res = 0
            for j in left:
                res += dfs(i+1, seen | set([j]))
            return res
        
        return dfs(0, set())