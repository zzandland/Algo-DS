class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N, dp = len(books), {}
        def dq(i: int, cur: int, mh: int) -> int:
            if i == N: return mh
            w, h = books[i]
            if (i, cur) not in dp:
                if cur+w > shelf_width:
                    dp[i, cur] = mh + dq(i+1, w, h)
                else:
                    dp[i, cur] = min(dq(i+1, cur+w, max(mh, h)), mh + dq(i+1, w, h))
            return dp[i, cur]
        return dq(0, 0, 0)