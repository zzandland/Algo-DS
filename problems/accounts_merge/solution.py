from collections import defaultdict

class UF:

    def __init__(self):
        self.parents = []
        self.id2email = {}
        self.email2id = {}
        self.id_ = -1
        
    def getId(self, email: str) -> int:
        if email not in self.email2id:
            self.id_ += 1
            self.parents.append(self.id_)
            self.email2id[email] = self.id_
            self.id2email[self.id_] = email
        return self.email2id[email]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = defaultdict(UF)
        
        def find(u: int, parents: List[int]) -> int:
            if parents[u] != u: parents[u] = find(parents[u], parents)
            return parents[u]
        
        def union(u: int, v: int, parents: List[int]) -> None:
            uf, vf = find(u, parents), find(v, parents)
            parents[uf] = vf
        
        for acc in accounts:
            name, emails = acc[0], acc[1:]
            uf = dic[name]
            fid = uf.getId(emails[0])
            for i in range(1, len(emails)):
                id_ = uf.getId(emails[i])
                union(fid, id_, uf.parents)
                    
        res = []
        
        for name, uf in dic.items():
            seen = set()
            parents = uf.parents
            for i in range(len(parents)):
                if i in seen: continue
                emails = [uf.id2email[i]]
                for j in range(i+1, len(parents)):
                    if j not in seen and find(i, parents) == find(j, parents):
                        emails.append(uf.id2email[j])
                        seen.add(j)
                res.append([name] + sorted(emails))
                        
        return res