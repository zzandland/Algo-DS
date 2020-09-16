class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 != 0: return False
        q = {sm//2}
        for n in nums:
            nq = set()
            for v in q:
                if v - n == 0: return True
                if v - n > 0: nq.add(v-n)
                nq.add(v)
            q = nq
        return False