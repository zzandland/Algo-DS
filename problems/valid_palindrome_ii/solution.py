class Solution:
    def validPalindrome(self, s: str) -> bool:
        def fn(skip: bool, l: int = 0, r: int = len(s)-1) -> bool:
            while l < r:
                if s[l] != s[r]:
                    if not skip: return fn(True, l+1, r) or fn(True, l, r-1)
                    return False
                l, r = l+1, r-1    
            return True    
        return fn(False)