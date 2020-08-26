class Solution:
    def trap(self, height: List[int]) -> int:
        left = list(range(len(height)))
        right = left[:]
        st = []
        for i, h in enumerate(height):
            while st and st[-1][1] <= h:
                right[st.pop()[0]] = i
            if st: left[i] = st[-1][0]
            st.append((i, h))
        i = 0
        res = 0
        while i < len(height):
            while height[left[i]] > height[right[i]] and right[i] != right[right[i]]: right[i] = right[right[i]]
            else:
                for j in range(i, right[i]):                
                    res += min(height[left[i]], height[right[i]]) - height[j]
                i = right[i] + 1
        return res