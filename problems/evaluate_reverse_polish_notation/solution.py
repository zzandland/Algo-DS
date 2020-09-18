class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }
        if not tokens: return 0
        st = []
        for c in tokens:
            if c.lstrip('-').isnumeric():
                st.append(int(c))
            else:
                a, b = st.pop(), st.pop()
                st.append(op[c](b, a))
        return st[-1]