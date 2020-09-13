class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        up = down = res = 0
        for a, b in zip(A, A[1:]):
            if down and a < b or a == b: up = down = 0
            up += int(a < b)
            down += int(a > b)
            if up and down: res = max(res, up + down + 1)
        return 0 if res < 3 else res