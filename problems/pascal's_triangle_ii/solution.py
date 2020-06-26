class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fn(arr: List[int], k: int) -> List[int]:
            if k == 0: return arr
            return fn([0] + [arr[i] + arr[i+1] for i in range(0, len(arr)-1)] + [0], k-1)
        return fn([0, 1, 0], rowIndex)[1:-1]