class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        out, used = [], [False] * 256
        for i in range(len(s)):
            if s[i] not in dic:
                if used[ord(t[i])]:
                    return False
                dic[s[i]] = t[i]
                used[ord(t[i])] = True
            out.append(dic[s[i]])
        return ''.join(out) == t