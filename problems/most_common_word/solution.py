class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        freq = Counter()
        for w in re.sub('\W', ' ', paragraph.lower()).split(' '):
            if w and w not in ban: freq[w] += 1
        return max(freq.items(), key=operator.itemgetter(1))[0]