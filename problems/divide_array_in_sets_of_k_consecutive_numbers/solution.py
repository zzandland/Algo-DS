class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N % k != 0: return False
        nums.sort()
        
        left = Counter(nums)
        end = Counter()
        
        for n in nums:
            if not left[n]: continue
            for i in range(k):
                if not left[n+i]: return False
                left[n+i] -= 1
        return True