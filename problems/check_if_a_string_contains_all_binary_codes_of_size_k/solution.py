class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        S, st = len(s), set()
        for i in range(k, S+1):
            st.add(s[i-k:i])
        return len(st) == 2**k    