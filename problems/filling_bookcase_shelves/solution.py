class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N = len(books)
        dp = [0]
        for i in range(N):
            w, j = books[i][0], i
            while j >= 0 and w <= shelf_width:
                j -= 1
                w += books[j][0]
            tmp = float('inf')
            for k in range(j+1, i+1):
                tmp = min(tmp, dp[k] + max(books[x][1] for x in range(k, i+1)))
            dp.append(tmp)
        return dp[-1]
 