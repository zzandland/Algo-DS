class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        mx = -1
        for i in range(len(A) - 2):
            mx = max(mx, A[i])
            if mx > A[i+2]: return False
        return True