class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        def fn(i: int, j: int) -> List[List[int]]:
            if j == 0: return [[]]
            if i == n: return []
            return [[nums[k]] + pst for k in range(i, n) for pst in fn(k+1, j-1)]
        return fn(0, k)