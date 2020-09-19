from collections import defaultdict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N = len(people)
        dic = defaultdict(list)
        res = [None]*N
        rem = {*range(N)}
        for h, k in people:
            dic[h].append(k)
        
        for h in sorted(dic):
            tmp = sorted(rem)
            for i in dic[h]:
                res[tmp[i]] = [h, i]
                rem.remove(tmp[i])
                
        return res