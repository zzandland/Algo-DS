class Solution:
    def calculate(self, s: str) -> int:
        ops = {
            '+': lambda a, b: int(a) + int(b),
            '-': lambda a, b: int(a) - int(b),
            '*': lambda a, b: int(a) * int(b),
            '/': lambda a, b: 0 if b == '0' else int(a) // int(b)
        }
        s = ''.join(list(filter(lambda x: x != ' ', s)))
        split = re.split('(\D)', s)
        
        st, i = [], 0
        
        # only handle mul and div first
        while i < len(split):
            c = split[i]
            if c.isnumeric() or c in ('+', '-'):
                st.append(c)
            elif c in ('*', '/'):
                a = st.pop()
                st.append(ops[c](a, split[i+1]))
                i += 1
            i += 1
        
        # go through the stack from bottom and cal
        res = st[0]
        for i in range(1, len(st), 2):
            res = ops[st[i]](res, st[i+1])
        return res