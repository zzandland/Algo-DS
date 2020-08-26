class Solution:
    def minWindow(self, S: str, T: str) -> str:
        start = -1
        ln = float('inf')
        s = t = 0
        while s < len(S):
            if S[s] == T[t]:
                t += 1
                if t == len(T):
                    end = s+1
                    t -= 1
                    while t >= 0:
                        if S[s] == T[t]: t -= 1
                        s -= 1
                    if end - s < ln: start, ln = s+1, end - s
            s += 1
        return '' if start == -1 else S[start:start+ln-1]