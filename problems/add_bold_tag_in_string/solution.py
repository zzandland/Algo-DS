class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        arr = [False]*len(s)
        def find(t: str) -> None:
            res, start = [], 0
            while True:
                idx = s.find(t, start, )
                if idx == -1: return res
                for i in range(idx, idx+len(t)):
                    arr[i] = True
                start = idx+1
        for w in dict:
            find(w)
        res, st = [], -1
        for i in range(len(s)):
            if not arr[i]:
                if st != -1:
                    res.append('<b>%s</b>' % s[st:i])
                    st = -1
                res.append(s[i])
            else:
                if st == -1: st = i
        if arr[-1]: res.append('<b>%s</b>' % s[st:len(arr)])
        return ''.join(res)