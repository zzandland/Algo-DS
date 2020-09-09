from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(nums)
        seq = Counter()
        
        for n in nums:
            if not left[n]: continue
            left[n] -= 1
            if seq[n-1] > 0:
                seq[n-1] -= 1
                seq[n] += 1
            elif left[n+1] and left[n+2]:
                left[n+1] -= 1
                left[n+2] -= 1
                seq[n+2] += 1
            else: return False
        return True