class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros, N = arr.count(0), len(arr)
        for i in range(N-1, -1, -1):
            if i+zeros < N:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i+zeros < N:
                    arr[i+zeros] = arr[i]