from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        q = deque([*s])
        def dfs() -> str:
            tmp = []
            while q:
                c = q.popleft()
                if c.isdigit():
                    val = []
                    while c != '[':
                        val.append(c)
                        c = q.popleft()
                    tmp.append(int(''.join(val)) * dfs())
                elif c == ']': return ''.join(tmp)
                else: tmp.append(c)
            return ''.join(tmp)
        return dfs()