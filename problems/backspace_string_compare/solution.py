class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        st, tt = [], []
        for s in S:
            if s == '#':
                if st: st.pop()
            else: st.append(s)    
        for t in T:
            if t == '#':
                if tt: tt.pop()
            else: tt.append(t)    
        print(st, tt)        
        return ''.join(st) == ''.join(tt)