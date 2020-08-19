class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        for i, w in enumerate(S.split()):
            if w[0].lower() in ('a', 'e', 'i', 'o', 'u'): nw = w + 'ma'
            else: nw = w[1:] + w[0] + 'ma'
            nw += 'a'*(i+1)
            res.append(nw)
        return ' '.join(res)