from collections import defaultdict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N, dic = len(people), defaultdict(list)
        for h, l in people:
            dic[h].append(l)
        st, res = set(range(N)), [None]*N
        for h in sorted(dic):
            tmp = sorted(st)
            for i in dic[h]:
                res[tmp[i]] = (h, i)
                st.remove(tmp[i])
        return res        