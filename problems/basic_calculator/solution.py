class Solution:
    def calculate(self, s: str) -> int:
        st, ch = [], ''
        for c in '(' + s + ')':
            if c != ' ':
                if c.isnumeric():
                    ch += c
                else:
                    if ch:
                        st.append(ch)
                        ch = ''
                    st.append(c)    
        st = st[::-1]
        def fn() -> int:
            add, out, c = True, 0, st.pop()
            while st and c != ')':
                if c == '(':
                    out += fn() if add else -1*fn()
                elif c == '+':
                    add = True    
                elif c == '-':
                    add = False
                else:
                    out += int(c) if add else -1*int(c)
                if st: c = st.pop()    
            return out
        return fn()