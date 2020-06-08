from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        q, st, buf = deque(s), [], ''
        while q:
            c = q.popleft()
            if c.isdigit():
                digit = ''
                while c.isdigit():
                    digit += c
                    c = q.popleft()
                st.append((int(digit), buf))
                buf = ''
            elif c == ']':
                mul, p = st.pop()
                buf = p + mul*buf
            else:
                buf += c
        return buf         