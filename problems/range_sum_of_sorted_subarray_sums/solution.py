class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        comb = []
        N = len(nums)
        for i in range(N):
            tmp = 0
            for j in range(i, N):
                tmp += nums[j]
                comb.append(tmp)
        return sum(sorted(comb)[left-1:right]) % (10**9+7)