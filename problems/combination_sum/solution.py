class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        def dq(i: int, n: int) -> List[List[int]]:
            if i == N and n == 0:
                return [[]]
            if i == N or n < 0:
                return []
            c = candidates[i]
            return [[c] + x for x in dq(i, n-c)] + dq(i+1, n)
        return dq(0, target)