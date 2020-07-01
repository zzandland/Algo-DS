class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def genAvail(i: int) -> List[int]:
            res = set()
            if i == 1:
                if 2 in seen: res.add(3)
                if 5 in seen: res.add(9)
                if 4 in seen: res.add(7)
            elif i == 2:
                if 5 in seen: res.add(8)
                res |= set([1, 4, 7, 5, 9, 6, 3])
            elif i == 3:
                if 2 in seen: res.add(1)
                if 5 in seen: res.add(7)
                if 6 in seen: res.add(9)
            elif i == 4:    
                if 5 in seen: res.add(6)
                res |= set([1, 2, 3, 5, 7, 8, 9])
            elif i == 5:
                res |= set([1, 2, 3, 4, 6, 7, 8, 9])
            elif i == 6:
                if 5 in seen: res.add(4)
                res |= set([3, 2, 1, 5, 7, 8, 9])
            elif i == 7:
                if 4 in seen: res.add(1)
                if 5 in seen: res.add(3)
                if 8 in seen: res.add(9)
            elif i == 8:
                if 5 in seen: res.add(2)
                res |= set([7,4,1,5,3,6,9])
            elif i == 9:
                if 6 in seen: res.add(3)
                if 5 in seen: res.add(1)
                if 8 in seen: res.add(7)
            if i in (1, 3, 7, 9): res |= set([2, 5, 4, 8, 6])
            return res - seen
        def dfs(i: int, k: int) -> int:
            if k == n: return 1
            res = 0
            for ni in genAvail(i):
                seen.add(ni)
                res += dfs(ni, k+1)
                seen.remove(ni)
            return int(m <= k) + res
        out = 0
        for i in range(1, 10):
            seen = set([i])
            out += dfs(i, 1)            
        return out