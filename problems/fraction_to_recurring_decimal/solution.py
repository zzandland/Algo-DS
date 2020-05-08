class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        dic, neg = {}, False
        if denominator < 0:
            denominator *= -1
            neg = not neg
        if numerator < 0:
            numerator *= -1    
            neg = not neg
        while denominator % 10 == 0 and numerator % 10 == 0:
            denominator //= 10
            numerator //= 10
        q, r1 = divmod(numerator, denominator)
        output = str(q) + '.'
        while r1 > 0:
            q, r2 = divmod(r1*10, denominator)
            if (r2, q) in dic:
                return '-'*int(neg) + output[:dic[(r2, q)]] + '(' + output[dic[(r2, q)]:] + ')'
            if (r2, q) not in dic: dic[(r2, q)] = len(output)
            output += str(q)
            r1 = r2
        return '-'*int(neg) + output[:2] + output[2:] if output[-1] != '.' else '-'*int(neg) + output[:-1]