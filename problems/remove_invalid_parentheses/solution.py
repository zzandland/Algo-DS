class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res, S, mx, dic = set(), len(s), 0, {'(': 1, ')': -1}
        def dfs(i: int, c: int, ss: str) -> None:
            nonlocal res, mx, dic
            if c < 0: return
            if i == S:
                if c == 0:
                    if len(ss) > mx: res, mx = set(), max(mx, len(ss))
                    if len(ss) == mx: res.add(ss)    
                return
            if s[i] not in ('(', ')'): return dfs(i+1, c, ss+s[i])
            dfs(i+1, c+dic[s[i]], ss+s[i]), dfs(i+1, c, ss)
        dfs(0, 0, '')    
        return res