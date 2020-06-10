class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        st, left, right = [], [-1]*N, [-1]*N
        for i, h in enumerate(height):
            while st and st[-1][1] < h:
                right[st.pop()[0]] = i
            if st:
                left[i] = st[-1][0]
            st.append((i, h))
        i = res = 0
        while i < N:
            if left[i] != -1 and right[i] != -1:
                hl, r = height[left[i]], right[i]
                while hl >= height[r] and right[r] != -1:
                    r = right[r]
                h = min(hl, height[r])
                for j in range(i, r):
                    res += h-height[j]
                i = r
            else:
                i += 1        
        return res        
            