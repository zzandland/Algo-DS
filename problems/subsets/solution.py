class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        tmp, res = [], []
        def fn(i: int) -> None:
            res.append(tmp[:])
            if i == N: return
            for j in range(i, N):
                tmp.append(nums[j])
                fn(j+1)
                tmp.pop()
        fn(0)
        return res