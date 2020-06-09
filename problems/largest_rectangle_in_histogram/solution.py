class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N, st, res = len(heights), [], 0
        left, right = [-1]*N, [N]*N
        for i, h in enumerate(heights):
            while st and st[-1][0] > h:
                right[st.pop()[1]] = i
            if st:
                left[i] = st[-1][1]
            st.append((h, i))
        for l, r, h in zip(left, right, heights):
            res = max(res, (r-l-1) * h)
        return res