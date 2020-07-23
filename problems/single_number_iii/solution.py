class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = set()
        for n in nums:
            if n in seen: seen.remove(n)
            else: seen.add(n)
        return list(seen)