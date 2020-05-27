class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            tmp = []
            for p in res:
                for i in range(len(p)+1):
                    tmp.append(p[:i] + [num] + p[i:])
            res = tmp        
        return res    