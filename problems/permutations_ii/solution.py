class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        q = [[]]
        for i, n in enumerate(nums):
            nq = []
            for p in q:
                for j in range(len(p)+1):
                    if j > 0 and n == p[j-1]: break
                    nq.append(p[:j]+[n]+p[j:])
            q = nq
        return q