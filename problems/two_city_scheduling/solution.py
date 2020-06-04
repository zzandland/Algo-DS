class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        costs.sort(key=lambda x: x[0]-x[1])
        return sum([c[0] for c in costs[:N//2]] + [c[1] for c in costs[N//2:]])