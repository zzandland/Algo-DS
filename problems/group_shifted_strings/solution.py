from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getDist(s: str) -> List[int]:
            res = []
            for a, b in zip(s, s[1:]):
                d = ord(b) - ord(a)
                if d < 0: d += 26
                res.append(d)
            return tuple(res)
        dic = defaultdict(list)
        # iterate string O(n)
        for s in strings:
            # save string as value and order as key to dict
            key = getDist(s)
            dic[key].append(s)
        # return values of the dict
        return dic.values()