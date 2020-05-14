class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0: return ['']
        comb = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        def fn(s: List[int]) -> List[str]:
            if len(s) > n: return []
            if len(s) == n: return [''.join(s)] if s[0] != '0' else []
            output = []
            for a, b in comb:
                if not s and n == 2 and a == '0': continue
                if not s and n % 2 == 1 and a in ('0', '1', '8'): output += fn([a])    
                else: output += fn([a] + s + [b])    
            return output        
        return fn([]) if n > 1 else ['0', '1', '8']