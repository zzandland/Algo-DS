class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st = []
        res = [0]*len(T)
        
        for i, t in enumerate(T):
            while st and st[-1][0] < t:
                d = st.pop()[1]
                res[d] = i-d
            st.append((t, i))
        return res