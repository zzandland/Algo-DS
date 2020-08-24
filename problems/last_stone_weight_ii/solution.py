class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for s in stones:
            dp = {i+s for i in dp} | {i-s for i in dp}
        return min([abs(i) for i in dp])