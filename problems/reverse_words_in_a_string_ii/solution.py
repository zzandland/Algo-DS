class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        left = right = 0
        while left < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            self.reverse(s, left, right - 1)    
            right += 1
            left = right
            
    def reverse(self, s: List[str], begin: int, end: int) -> None:
        while end > begin:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1