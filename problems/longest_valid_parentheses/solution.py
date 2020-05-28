class Solution:
    def longestValidParentheses(self, s: str) -> int:
        S, mx, st = len(s), 0, [-1]
        for i, c in enumerate(s):
            if c == '(': st.append(i)
            else:
                last = st.pop()
                if not st: st.append(i)
                else: mx = max(mx, i - st[-1])
        return mx