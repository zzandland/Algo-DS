class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        st = []
        res = [0]*n
        for x in logs:
            fn, com, ts = x.split(':')
            fn, ts = int(fn), int(ts)
            if st: res[st[-1]] += ts - p
            p = ts
            if com == 'start':
                st.append(fn)
            else:
                res[st[-1]] += 1
                p += 1
                st.pop()
        return res