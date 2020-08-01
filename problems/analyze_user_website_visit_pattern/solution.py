from collections import defaultdict, Counter

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visit_per_user = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            visit_per_user[u].append(w)
        order_freq = defaultdict(set)
        def dfs(i: int, tmp: List[str]) -> None:
            if len(tmp) == 3:
                order_freq[tuple(tmp)].add(user)
                return
            if i == len(visits): return
            tmp.append(visits[i])
            dfs(i+1, tmp)
            tmp.pop()
            dfs(i+1, tmp)
        for user in visit_per_user:
            visits = visit_per_user[user]
            dfs(0, [])
        return min(order_freq.items(), key=lambda x: (-len(x[1]), x[0]))[0]