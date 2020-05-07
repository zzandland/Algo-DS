from collections import Counter

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.dic = {}
        self.s = ''
        for i, s in enumerate(sentences):
            b = ''
            for c in s:
                b += c
                if b not in self.dic: self.dic[b] = Counter()
                self.dic[b][s] = times[i]

    def input(self, c: str) -> List[str]:
        if c == '#':
            kw, b = self.s, ''
            for c in self.s:
                b += c
                self.dic[b][kw] += 1
            self.s = ''    
            return []    
        else:    
            self.s += c
            if self.s not in self.dic: self.dic[self.s] = Counter()
            return [s for s, c in sorted(self.dic[self.s].items(), key=lambda x: (-x[1], x[0]))[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)