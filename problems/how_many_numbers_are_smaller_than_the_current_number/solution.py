class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = [0]*101
        for num in nums:
            c[num] += 1
        p = [0]*101
        for i in range(1, 101):
            p[i] += c[i-1] + p[i-1]
        return [p[num] for num in nums]    