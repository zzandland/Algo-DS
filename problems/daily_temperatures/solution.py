class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res, st = [0]*len(T), []
        for i, t in enumerate(T):
            while st and st[-1][0] < t:
                _, j = st.pop()
                res[j] = i-j
            st.append((t, i))    
        return res        