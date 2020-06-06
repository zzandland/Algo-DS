class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        st, nxt = [], [-1]*N*2
        for i, n in enumerate(nums+nums):
            while st and st[-1][0] < n:
                nxt[st.pop()[1]] = n
            st.append((n, i))        
        return [nxt[i] for i, n in enumerate(nums)]