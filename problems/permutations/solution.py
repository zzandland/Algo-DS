class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        q = [[]]
        for n in nums:
            nq = []
            for perm in q:
                for i in range(len(perm)+1):
                    nq.append(perm[:i] + [n] + perm[i:])
            q = nq
        return q