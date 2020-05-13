from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        q = deque(list(s))
        def fn() -> str:
            s = ''
            while q:
                c = q.popleft()
                if c == ']': return s
                elif c.isdigit():
                    n = ''
                    while c.isdigit():
                        n += c
                        c = q.popleft()
                    s += (fn()*int(n))
                else: s += c
            return s        
        return fn()