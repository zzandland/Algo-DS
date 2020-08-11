class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for c in citations:
            if res >= c: return res
            res += 1
        return res