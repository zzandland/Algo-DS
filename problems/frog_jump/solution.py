class Solution:
    def canCross(self, stones: List[int]) -> bool:
        idx = {n: i for i, n in enumerate(stones)}
        if 1 not in idx: return False
        N = len(stones)
        q = deque([(-1, 1)])
        seen = set()
        while q:
            pos, k = q.popleft()
            pos *= -1
            if pos == stones[-1]: return True
            if (pos, k) in seen or pos not in idx: continue
            seen.add((pos, k))
            q.append((-pos-k-1, k+1))
            q.append((-pos-k, k))
            q.append((-pos-k+1, k-1))
        return False