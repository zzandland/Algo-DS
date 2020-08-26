class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i = 0
        while i < len(A)-1 and A[i] == A[i+1]:
            i += 1
        
        if i == len(A)-1: return True
        asc = A[i] < A[i+1]
        while i < len(A)-1:
            if asc and A[i] > A[i+1]: return False
            elif not asc and A[i] < A[i+1]: return False
            i += 1
        return True