class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def fn(c: int, s: int) -> List[str]:
            if c < 0: return []
            if len(s) == n*2: return [s] if c == 0 else []
            return fn(c+1, s+'(') + fn(c-1, s+')')
        return fn(0, '')