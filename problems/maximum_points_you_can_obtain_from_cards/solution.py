from heapq import heappush, heappop

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix = [0]
        for n in cardPoints:
            prefix.append(prefix[-1] + n)
        res = 0
        window = len(cardPoints) - k
        for i in range(window-1, len(cardPoints)):
            res = max(res, prefix[-1] - prefix[i+1] + prefix[i-window+1])
        return res