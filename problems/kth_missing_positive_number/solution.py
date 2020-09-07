class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 1
        for n in arr:
            diff = n - prev
            if k > diff:
                k -= diff
                prev = n + 1
            else:
                return prev + k - 1
        return arr[-1] + k