class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def recurse(n: int, diff: int, tmp: str) -> None:
            nonlocal output
            if n == 0 and diff == 0:
                output.append(tmp)
                return
            if n > 0:
                recurse(n - 1, diff + 1, tmp + '(')
            if diff > 0:
                recurse(n, diff - 1, tmp + ')')    
        recurse(n, 0, "")
        return output