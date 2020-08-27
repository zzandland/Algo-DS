class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        ln = 0
        def dfs(i: int, cnt: int, tmp: List[str]) -> None:
            nonlocal res, ln
            if cnt < 0: return
            if i == len(s):
                if cnt != 0: return
                if len(tmp) > ln:
                    res = set()
                    ln = len(tmp)
                if len(tmp) == ln:
                    res.add(''.join(tmp))
                return
            if s[i] == '(':
                tmp.append('(')
                dfs(i+1, cnt+1, tmp)
                tmp.pop()
                dfs(i+1, cnt, tmp)
            elif s[i] == ')':
                tmp.append(')')
                dfs(i+1, cnt-1, tmp)
                tmp.pop()
                dfs(i+1, cnt, tmp)
            else:
                tmp.append(s[i])
                dfs(i+1, cnt, tmp)
                tmp.pop()
        dfs(0, 0, [])
        return res