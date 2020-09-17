class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        st = []
        left = [-1]*N
        right = [N]*N
        for i, h in enumerate(heights):
            while st and st[-1][0] > h:
                right[st.pop()[1]] = i
            if st: left[i] = st[-1][1]
            st.append((h, i))
        
        return max([h * (right[i] - left[i] - 1) for i, h in enumerate(heights)] or [0])