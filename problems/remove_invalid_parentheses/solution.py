class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = {''}
        ln = 0
        def dfs(i: int, c: int, tmp: [str]) -> None:
            nonlocal res, ln
            if c < 0: return
            if i == len(s):
                if c == 0:
                    if len(tmp) > ln:
                        res.clear()
                        ln = len(tmp)
                    if len(tmp) == ln:
                        res.add(''.join(tmp))
                return
            if s[i] == '(':
                tmp.append('(')
                dfs(i+1, c+1, tmp)
                tmp.pop()
                dfs(i+1, c, tmp)
            elif s[i] == ')':
                tmp.append(')')
                dfs(i+1, c-1, tmp)
                tmp.pop()
                dfs(i+1, c, tmp)
            else:
                tmp.append(s[i])
                dfs(i+1, c, tmp)
                tmp.pop()
        dfs(0, 0, [])
        return res