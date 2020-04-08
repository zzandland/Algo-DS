from collections import Counter
import re
import heapq

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt, ban, hp = Counter(), set(banned), []
        for wd in re.split("[!?',;.'\s]", paragraph):
            wdL = wd.lower()
            if wdL not in banned and wdL != '':
                cnt[wdL] += 1
        for w, c in cnt.items():
            heapq.heappush(hp, (-c, w))
        return heapq.heappop(hp)[1]