from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            st = ''.join(sorted(s))
            dic[st].append(s)
        return dic.values()    