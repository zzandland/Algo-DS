class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N, dic, sm = len(nums), {0:-1}, 0
        for i, n in enumerate(nums):
            sm += n
            if k != 0: sm %= k
            if sm in dic and i-dic[sm] > 1: return True
            dic.setdefault(sm, i)
        return False        