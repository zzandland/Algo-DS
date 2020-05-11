class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        L, climb = len(A), True
        for i in range(L-1):
            if climb and A[i] >= A[i+1]:
                if i == 0: return False
                climb = False
            if not climb and A[i] <= A[i+1]: return False    
        return not climb    