class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            name, domain = S.lower().split('@')
            return name[0] + '*'*5 + name[-1] + '@' + domain
        s = re.sub('[\+\-() ]', '', S)
        cc, local = s[:len(s)-10], s[-4:]
        ccs = '+' + '*' * len(cc) + '-' if cc else ''
        return ccs + '***-***-' + local