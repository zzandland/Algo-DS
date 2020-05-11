class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '['}
        st = []
        for c in s:
            if c in ('(', '{', '['): st.append(c)
            else:
                if not st or dic[c] != st[-1]: return False
                st.pop()
        return not st