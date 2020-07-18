from heapq import heappush, heappop

class Solution:
    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        stations.append((target, 0))
        pq = []
        
        res = prev = 0
        # as passing through stations O(n)
        for loc, charge in stations:
            tank -= loc - prev
            # if fuel runs out before getting to this loc greedily refuel
            while pq and tank < 0:
                tank -= heappop(pq)
                res += 1
            # if tank is empty and cant get to loc
            if tank < 0: return -1
            # save gas in this station
            heappush(pq, -charge)
            prev = loc
        return res