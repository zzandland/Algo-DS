from collections import defaultdict
import heapq

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        W, st = len(wordlist), set(wordlist)
        diff, hp = {}, []
        def cntDiff(s1: str, s2: str) -> int:
            return sum([1 for i in range(6) if s1[i] == s2[i]])
        for i, w1 in enumerate(wordlist):
            for j in range(i):
                w2 = wordlist[j]
                diff.setdefault(w1, defaultdict(set))
                diff.setdefault(w2, defaultdict(set))
                cnt = cntDiff(w1, w2)
                diff[w1][cnt].add(w2)
                diff[w2][cnt].add(w1)
                heapq.heappush(hp, (-cnt, w1))
                heapq.heappush(hp, (-cnt, w2))
        useHp = True        
        for _ in range(10):
            if useHp:
                ct, w = heapq.heappop(hp)
                while w not in st:
                    ct, w = heapq.heappop(hp)
                if ct == 0: useHp = False   
            else: w = random.choice(list(st))        
            cnt = master.guess(w)
            if cnt == 6: break
            st.remove(w)
            if cnt > 0:
                for i in range(cnt):
                    st -= diff[w][i]
            else:
                for i in range(1, 7):
                    st -= diff[w][i]        