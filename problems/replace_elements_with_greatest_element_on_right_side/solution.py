class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            prev = mx
            mx = max(mx, arr[i])
            arr[i] = prev
        arr[-1] = -1
        return arr