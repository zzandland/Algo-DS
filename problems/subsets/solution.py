class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def fn(i: int, st: List[int]) -> List[int]:
            if i == len(nums): return []
            out = [st]
            for j in range(i+1, len(nums)):
                out += fn(j, st+[nums[j]])
            return out    
        return fn(-1, [])