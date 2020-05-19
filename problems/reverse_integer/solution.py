class Solution:
    def reverse(self, x: int) -> int:
        st, res, neg = [], 0, False
        if x < 0:
            x *= -1
            neg = True
        while x > 0:
            x, r = divmod(x, 10)
            st.append(r)
        for i, d in enumerate(st[::-1]):
            res += d * (10**i)
        if res >= int('7FFFFFFF', 16): return 0
        return res * (-1 if neg else 1)