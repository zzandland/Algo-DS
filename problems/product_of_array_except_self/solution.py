class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, run = [], 1
        for n in nums:
            left.append(run)
            run *= n
        right = []
        run = 1
        for n in nums[::-1]:
            right.append(run)
            run *= n
        return [a*b for a, b in zip(left, right[::-1])]