from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # filter out non letter chars O(paragraph)
        normalized = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
        banned_st = set(banned)
        cnt = Counter()
        for word in normalized.split():
            if word and word not in banned_st:
                cnt[word] += 1
                
        return max(cnt.items(), key=operator.itemgetter(1))[0]