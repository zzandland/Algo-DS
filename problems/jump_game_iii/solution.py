class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def fn(i: int) -> bool:
            if not (0 <= i < len(arr)) or arr[i] < 0: return False
            if arr[i] == 0: return True
            arr[i] = -arr[i]
            return fn(i + arr[i]) or fn(i - arr[i])
        return fn(start)