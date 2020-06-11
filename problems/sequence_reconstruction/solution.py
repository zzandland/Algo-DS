from collections import defaultdict

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        frm, to, V = defaultdict(set), defaultdict(set), set()
        for seq in seqs:
            V |= set(seq)
            for u, v in zip(seq, seq[1:]):
                frm[u].add(v)
                to[v].add(u)
        q, res = [n for n in V if n not in to], []
        while q:
            if len(q) > 1:
                return False
            n = q.pop()
            res.append(n)
            V.remove(n)
            for nn in frm[n]:
                to[nn].remove(n)
                if not to[nn]:
                    q.append(nn)
        return org == res and not V