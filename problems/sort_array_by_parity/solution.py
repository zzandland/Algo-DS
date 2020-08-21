class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = sum([1 for v in A if v & 1 == 0])
        i = 0
        while i < odd and odd < len(A):
            if A[i] & 1 == 0:
                i += 1
            else:
                A[odd], A[i] = A[i], A[odd]
                odd += 1
        return A