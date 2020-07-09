class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st = []
        nxt = [0]*len(T)
        # iterate the temps and get next greater val O(n)
        for i, temp in enumerate(T):
            while st and st[-1][0] < temp:
                _, prev = st.pop()
                nxt[prev] = i - prev
            st.append((temp, i))
        return nxt