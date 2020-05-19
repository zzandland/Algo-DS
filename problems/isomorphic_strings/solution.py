class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        aDic, bDic = {}, {}
        for i in range(len(s)):
            aDic.setdefault(s[i], t[i])
            bDic.setdefault(t[i], s[i])
            if t[i] != aDic[s[i]] or s[i] != bDic[t[i]]: return False
        return True