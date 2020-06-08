class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st, res = [], [0]*len(T)
        for i, t in enumerate(T):
            while st and st[-1][1] < t:
                j, _ = st.pop()
                res[j] = i-j
            st.append((i, t))    
        return res    