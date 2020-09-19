class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        b = Counter(c.values())
        mx = max(b)
        
        return max(len(tasks), (n+1) * (mx-1) + b[mx])