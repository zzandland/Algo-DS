from collections import defaultdict

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        dic, res = defaultdict(list), set()
        for p in phrases:
            tmp = p.split()
            dic[tmp[0]].append(p)
        for p in phrases:
            tmp = p.split()
            for ph in dic[tmp[-1]]:
                if ph == p and dic[tmp[-1]].count(ph) > 1:
                    res.add(p)
                if ph != p:
                    rest = ' '.join(ph.split()[1:])
                    res.add(p + ' ' + rest if rest else p)
        return sorted(res)