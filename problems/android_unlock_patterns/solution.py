class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        visited, res = set(), 0
        fives = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        def travel(x: int) -> set:
            if x in [1, 3, 7, 9]: res = set([2, 4, 5, 6, 8])
            elif x in [2, 8]: res = set([1, 3, 4, 5, 6, 7, 9])
            elif x in [4, 6]: res = set([1, 2, 3, 5, 7, 8, 9])
            else: res = set([1, 2, 3, 4, 6, 7, 8, 9])
            if 5 in visited: res.add(fives[x])    
            if x == 1:
                if 2 in visited: res.add(3)
                if 4 in visited: res.add(7)    
            elif x == 3:
                if 2 in visited: res.add(1) 
                if 6 in visited: res.add(9)
            elif x == 7:
                if 4 in visited: res.add(1) 
                if 8 in visited: res.add(9)
            elif x == 9:
                if 6 in visited: res.add(3)        
                if 8 in visited: res.add(7)
            return res - visited
        def dfs(x: int, l: int) -> None:
            nonlocal res
            if l >= m: res += 1
            if l == n: return
            for nxt in travel(x):
                visited.add(nxt)
                dfs(nxt, l+1)
                visited.remove(nxt)
        for i in range(1, 10):
            visited.add(i)
            dfs(i, 1)
            visited.remove(i)
        return res    