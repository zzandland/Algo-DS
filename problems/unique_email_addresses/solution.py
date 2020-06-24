class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            local, domain = e.split('@')
            tmp = []
            for c in local:
                if c == '+': break
                if c != '.': tmp.append(c)
            res.add('%s@%s' % (''.join(tmp), domain))
        return len(res)