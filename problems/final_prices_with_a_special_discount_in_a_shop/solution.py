class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        nxt, st = [-1]*len(prices), []
        for i, p in enumerate(prices):
            while st and st[-1][0] >= p:
                nxt[st.pop()[1]] = i
            st.append((p, i))
        return [p-prices[nxt[i]] if nxt[i] != -1 else p for i, p in enumerate(prices)]