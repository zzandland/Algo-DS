from collections import defaultdict

class Solution:
    def candy(self, ratings: List[int]) -> int:
        R = len(ratings)
        dp, dic = [1]*R, defaultdict(list)
        for i, r in enumerate(ratings):
            if r > 0: dic[r].append(i)
        for r in sorted(dic):
            for i in dic[r]:
                l = dp[i-1] if i > 0 and ratings[i-1] < ratings[i] else 0
                r = dp[i+1] if i < R-1 and ratings[i+1] < ratings[i] else 0
                dp[i] = max(l, r) + 1
        return sum(dp)