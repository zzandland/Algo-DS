class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0)
        
    def helper(self, s: List[str], i: int) -> None:    
        if i == len(s) // 2: return
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        self.helper(s, i+1)