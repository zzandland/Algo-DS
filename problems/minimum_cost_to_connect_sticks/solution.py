import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        output = 0
        while len(sticks) > 1:
            sum_ = sum([heapq.heappop(sticks) for _ in range(2)])
            output += sum_
            heapq.heappush(sticks, sum_)
        return output    