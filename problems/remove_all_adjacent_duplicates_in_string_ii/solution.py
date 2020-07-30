class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        i = 0
        while i < len(s):
            if not st or s[i] != st[-1][0]: st.append([s[i], 1])
            else: st[-1][1] += 1
            if st[-1][1] == k: st.pop()
            i += 1
        return ''.join([c*cnt for c, cnt in st])