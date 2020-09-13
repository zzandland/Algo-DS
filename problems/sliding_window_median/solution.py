import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = []
        res = []
        for i, n in enumerate(nums):
            bisect.insort_left(window, n)
            if len(window) == k:
                m = len(window) // 2
                if k & 1 == 0: res.append((window[m-1] + window[m]) / 2)
                else: res.append(window[m])
                window.pop(bisect.bisect_left(window, nums[i-k+1]))
        return res