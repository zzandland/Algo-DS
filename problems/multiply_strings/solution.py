class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        A, B = len(num1), len(num2)
        muls, a, b = [], num1[::-1], num2[::-1]
        for i in range(B):
            lst, lft = ['0']*i, 0
            for j in range(A):
                c = str(int(b[i]) * int(a[j]) + lft)
                if len(c) == 2:
                    lft = int(c[0])
                    lst.append(c[1])
                else:
                    lft = 0    
                    lst.append(c)
            if lft > 0: lst.append(str(lft))
            muls.append(''.join(lst))    
        output, lft = [], 0
        for k in range(len(max(muls, key=lambda x: len(x)))):
            sm = 0
            for mul in muls:
                if len(mul) > k:
                    sm += int(mul[k])
            q, r = divmod(sm+lft, 10)        
            output.append(str(r))
            lft = q
        if lft > 0: output.append(str(lft))    
        return ''.join(output[::-1])