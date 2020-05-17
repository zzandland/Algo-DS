class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3: return True
        l, r, skipped = 0, len(s)-1, False
        def isPal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]: return False
                l, r = l+1, r-1
            return True    
        while l < r:
            if s[l] == s[r]:
                l, r = l+1, r-1
            else:
                return isPal(l+1, r) or isPal(l, r-1)
        return True        