class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n: int, c: int) -> List[str]:
            if n == 0 and c == 0: return ['']
            if c > n or c < 0: return []
            return ['(' + w for w in dfs(n, c+1)] + [')' + w for w in dfs(n-1, c-1)]
        return dfs(n, 0)