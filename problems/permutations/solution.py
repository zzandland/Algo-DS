class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = [[]]
        for n in nums:
            nres = []
            for p in res:
                for i in range(len(p)+1):
                    nres.append(p[:i]+[n]+p[i:])
            res = nres
        return res