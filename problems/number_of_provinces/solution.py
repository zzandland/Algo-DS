from collections import deque

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # dfs all connected friends O(N)
        seen = set()
        def dfs(n: int) -> None:
            if n in seen: return
            seen.add(n)
            for i in range(len(M)):
                if M[n][i]: dfs(i)
        res = 0
        for i in range(len(M)):
            if i not in seen:
                # bfs all connected friends O(N)
                res += 1
                q = deque([i])
                while q:
                    n = q.popleft()
                    if n in seen: continue
                    seen.add(n)
                    for j in range(len(M)):
                        if M[n][j]: q.append(j)
        return res