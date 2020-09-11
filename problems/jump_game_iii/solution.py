from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        seen = {start}
        
        while q:
            idx = q.popleft()
            if arr[idx] == 0: return True
            l, r = idx - arr[idx], idx + arr[idx]
            if l >= 0 and l not in seen:
                seen.add(l)
                q.append(l)
            if r < len(arr) and r not in seen:
                seen.add(r)
                q.append(r)
        return False