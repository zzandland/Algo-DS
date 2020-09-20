class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        res = float('inf')
        run = 0
        for i, p in enumerate(cardPoints):
            if i >= N-k: run -= cardPoints[i-N+k]
            run += p
            if i >= N-k-1: res = min(res, run)
        return sum(cardPoints) - res