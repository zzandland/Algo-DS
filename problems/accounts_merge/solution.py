from collections import defaultdict, Counter

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = defaultdict(set)
        for acc in accounts:
            for i in range(1, len(acc)):
                dic[acc[i]] |= set(acc[1:i]+acc[i+1:])
        visited, res = set(), []
        def dfs(email: str) -> List[str]:
            if email in visited: return []
            visited.add(email)
            res2 = [email]
            for nxt in dic[email]: res2 += dfs(nxt)
            return res2
        for acc in accounts:
            emails, rec = acc[1:], []
            for e in emails: 
                rec += dfs(e)
            if rec: res.append([acc[0]] + sorted(rec))
        return res