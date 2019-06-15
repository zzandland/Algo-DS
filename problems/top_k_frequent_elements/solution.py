class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 0
            count_map[num] += 1    
        lst = []
        for num, cnt in count_map.items():
            heapq.heappush(lst, (-1 * cnt, num))
        output = []
        for i in range(k):
            output.append(heapq.heappop(lst)[1])
        return output    