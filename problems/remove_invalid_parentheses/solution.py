class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        S, output, mx = len(s), set(), 0
        def fn(i: int, cnt: int, substr: str) -> None:
            nonlocal mx, output
            if cnt < 0:  return
            if i == S: 
                if cnt == 0:
                    if len(substr) > mx: 
                        output = set()
                        mx = len(substr)
                    if len(substr) == mx:    
                        output.add(substr)
                return
            if s[i] not in ('(', ')'): return fn(i+1, cnt, substr+s[i])
            nxt = cnt + 1 if s[i] == '(' else cnt - 1
            fn(i+1, nxt, substr+s[i])
            fn(i+1, cnt, substr)
        fn(0, 0, '')
        return list(output)