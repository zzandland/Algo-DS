class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        S, output, mx = len(s), set(), 0
        def fn(i: int, c: int, run: str) -> List[str]:
            nonlocal mx, output
            if c < 0: return
            if i == S:
                if c > 0: return
                if len(run) > mx:
                    mx = len(run)
                    output = set()
                if len(run) == mx: output.add(run)    
                return
            if s[i] == '(':
                fn(i+1, c+1, run+s[i])
                fn(i+1, c, run)
            elif s[i] == ')':
                fn(i+1, c-1, run+s[i])
                fn(i+1, c, run)
            else: fn(i+1, c, run+s[i])
        fn(0, 0, '')
        return list(output)