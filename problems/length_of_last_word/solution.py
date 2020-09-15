class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split()
        if not sp: return 0
        return len(sp[-1])