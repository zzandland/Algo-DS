class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        mxIdx = lambda i: max(range(i), key=lambda x: A[x]) 
        
        res = []
        for i in range(len(A)-1, 0, -1):
            idx = mxIdx(i+1)
            if idx == i: continue
            if idx > 0:
                res.append(idx+1)
                A = A[:idx+1][::-1] + A[idx+1:]
            res.append(i+1)
            A = A[:i+1][::-1] + A[i+1:]
        return res