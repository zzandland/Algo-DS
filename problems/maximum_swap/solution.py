class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10: return num
        digits = [int(d) for d in str(num)]
        nxt = [-1]*len(digits)
        st = []
        for i, n in enumerate(digits):
            while st and n >= st[-1][1]: nxt[st.pop()[0]] = i
            st.append((i, n))
        l = r = 0
        for i, n in enumerate(nxt):
            if n != -1:
                l, r = i, n
                while nxt[r] != -1: r = nxt[r]
                if digits[l] < digits[r]: break
        digits[l], digits[r] = digits[r], digits[l]
        return int(''.join(map(str, digits)))