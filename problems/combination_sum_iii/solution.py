class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(i: int, sm: int, tmp: [int]) -> None:
            nonlocal res
            if sm > n: return
            if sm == n:
                if len(tmp) == k: res.append(tmp[:])
                return
            for j in range(i+1, 10):
                tmp.append(j)
                dfs(j, sm+j, tmp)
                tmp.pop()
        dfs(0, 0, [])
        return res