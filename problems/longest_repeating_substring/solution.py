class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        def search(k: int) -> bool:
            seen = set()
            for i in range(k, len(S)+1):
                tmp = S[i-k:i]
                if tmp in seen: return True
                seen.add(tmp)
            return False
        
        l, r = 0, len(S)
        while l <= r:
            m = l + (r-l)//2
            if not search(m): r = m-1
            else: l = m+1
        return min(l, r)