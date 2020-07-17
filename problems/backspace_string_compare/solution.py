class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def delete(string: str, i: int) -> int:
            if i == -1: return -1
            cnt = 0
            while i >= 0:
                if string[i] == '#': cnt += 1
                elif cnt == 0: break
                else: cnt -= 1
                i -= 1
            return i
        s, t = len(S)-1, len(T)-1
        while s >= 0 and t >= 0:
            s, t = delete(S, s), delete(T, t)
            if s == -1 and t == -1: return True
            if S[s] != T[t]: return False
            s -= 1
            t -= 1
        s, t = delete(S, s), delete(T, t)
        return s == -1 and t == -1