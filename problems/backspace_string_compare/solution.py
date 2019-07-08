class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_s, T_s = [], []
        for c in S:
            if c == '#':
                if S_s:
                    S_s.pop()
            else:
                S_s.append(c)
        for c in T:
            if c == '#':
                if T_s:
                    T_s.pop()
            else:
                T_s.append(c)
        return ''.join(S_s) == ''.join(T_s)    