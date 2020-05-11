class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def skip(i: int, s: str) -> int:
            cnt = 0
            while i >= 0:
                if s[i] == '#': cnt += 1
                else:
                    if cnt == 0: return i    
                    cnt -= 1
                i -= 1    
            return i    
        s, t, sc, tc = len(S)-1, len(T)-1, 0, 0
        while s >= 0 or t >= 0:
            s = skip(s, S)
            t = skip(t, T)
            if s == -1 and t == -1: return True
            if s < 0 or t < 0 or S[s] != T[t]: return False
            s, t = s-1, t-1
        return True    