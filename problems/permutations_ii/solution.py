class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        q = [[]]
        for n in nums:
            nq = []
            for perm in q:
                for i in range(len(perm) + 1):
                    if i > 0 and n == perm[i-1]: break
                    nq.append(perm[:i] + [n] + perm[i:])
            q = nq
        return q