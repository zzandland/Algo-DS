class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def fn(i: int, c: int) -> List[str]:
            if i == n and c == 0:
                return ['']
            if i > n or c < 0:
                return []
            return ['(' + s for s in fn(i+1, c+1)] + [')' + s for s in fn(i, c-1)]
        return fn(0, 0)