class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total = sum([1*a if d else -1*a for d, a in shift])
        i = -(total % len(s))
        return s[i:]+s[:i]