class Solution:
    def removeDuplicates(self, S: str) -> str:
        found = True
        while found:
            found = False
            tmp, i = [], 0
            while i < len(S)-1:
                if S[i] == S[i+1]:
                    found = True
                    i += 2
                else:
                    tmp.append(S[i])
                    i += 1
            if i < len(S): tmp.append(S[i])
            S = ''.join(tmp)
        return S