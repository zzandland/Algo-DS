class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums += nums
        st = []
        nxt = [-1]*N*2
        for i, n in enumerate(nums):
            while st and st[-1][1] < n:
                nxt[st.pop()[0]] = n
            st.append((i, n))
        return nxt[:N]