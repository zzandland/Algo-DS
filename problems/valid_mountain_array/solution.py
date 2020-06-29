class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        up, seen = True, False
        for i in range(1, len(A)-1):
            if A[i] == A[i-1]: return False
            if A[i-1] < A[i] and A[i] > A[i+1]:
                if up:
                    seen = True
                    up = False
                else: 
                    return False
            elif not (A[i-1] < A[i] < A[i+1] and up) and not (A[i-1] > A[i] > A[i+1] and not up): return False
        return seen