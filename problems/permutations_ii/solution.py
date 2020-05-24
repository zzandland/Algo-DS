class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in sorted(nums):
            tmp = []
            for p in res:
                for i in range(len(p)+1):
                    tmp.append(p[:i]+[n]+p[i:])
                    if i < len(p) and p[i] == n: break
            res = tmp            
        return res