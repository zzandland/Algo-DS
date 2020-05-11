class Solution:
    def nextClosestTime(self, time: str) -> str:
        h, m = time.split(':')
        digits = [int(c) for c in list(time) if c.isdigit()]
        sort = sorted(set(digits))
        dic, mn = {e: i for i, e in enumerate(sort)}, sort[0]
        nxt = dic[digits[3]]+1
        if nxt < len(sort): return '{}:{}{}'.format(h, digits[2], sort[nxt])
        nxt = dic[digits[2]]+1
        if nxt < len(sort) and sort[nxt] < 6:
            return '{}:{}{}'.format(h, sort[nxt], mn)
        nxt = dic[digits[1]]+1
        if nxt < len(sort):
            if digits[0] < 2: return '{}{}:{}{}'.format(digits[0], sort[nxt], mn, mn)
            if digits[0] == 2 and sort[nxt] <= 4:
                return '{}{}:{}{}'.format(digits[0], sort[nxt], mn, mn)
        nxt = dic[digits[0]]+1    
        if nxt < len(sort) and sort[nxt] <= 2: return '{}{}:{}{}'.format(sort[nxt], mn, mn, mn)
        return '{}{}:{}{}'.format(mn, mn, mn, mn)