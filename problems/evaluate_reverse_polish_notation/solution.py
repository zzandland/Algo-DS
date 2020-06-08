from operator import add, mul, sub

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        st, dic = [], {'+': add, '-': sub, '*': mul, '/': lambda a, b: int(a / b)}
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                b, a = st.pop(), st.pop()
                op = dic[t](int(a), int(b))
                st.append(dic[t](int(a), int(b)))
            else:
                st.append(t)    
        return st[0]