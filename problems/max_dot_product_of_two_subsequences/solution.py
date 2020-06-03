class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        I, J = len(nums1), len(nums2)
        dp = [[None]*J for _ in range(I)]
        def dq(i: int, j: int, ) -> int:
            if i == I or j == J: return float('-inf')
            if dp[i][j] is None:
                prod = nums1[i] * nums2[j]
                dp[i][j] = max(prod, prod + dq(i+1, j+1), dq(i+1, j), dq(i, j+1))
            return dp[i][j]
        return dq(0, 0)                   