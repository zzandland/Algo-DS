class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        S = len(s)
        for i in range(S//2):
            s[i], s[S-i-1] = s[S-i-1], s[i]