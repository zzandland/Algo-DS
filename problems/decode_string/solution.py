from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        q = deque(s)
        def dfs() -> str:
            res = []
            while q:
                c = q.popleft()
                if c == ']': return ''.join(res)
                elif c.isdigit():
                    num = c
                    c = q.popleft()
                    while c.isdigit():
                        num += c
                        c = q.popleft()
                    res.append(int(num) * dfs())
                else: res.append(c)
            return ''.join(res)
        return dfs()