class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        N = len(heights)
        right, left = [N]*N, [-1]*N
        st, res = [], 0
        for i, h in enumerate(heights):
            while st and st[-1][1] > h:
                right[st.pop()[0]] = i
            if st:
                left[i] = st[-1][0]
            st.append((i, h))
        return max([(right[i] - left[i] - 1) * h for i, h in enumerate(heights)])