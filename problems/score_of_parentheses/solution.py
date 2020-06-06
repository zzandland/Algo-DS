from collections import deque

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        st = [0]
        for s in S:
            if s == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(1, v*2)
        return st.pop()        