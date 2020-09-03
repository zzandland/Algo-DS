class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gas = gas + gas
        cost = cost + cost
        res = tank = 0
        for i in range(N*2):
            if i - N == res: return res
            tank += gas[i] - cost[i]
            if tank < 0:
                res = i+1
                tank = 0
        return -1