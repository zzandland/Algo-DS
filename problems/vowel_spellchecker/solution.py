class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        perfect = set()
        capital = defaultdict(list)
        vowel = defaultdict(list)
        
        to_vowel = lambda s: re.sub('[aeiou]', '*', s.lower())
        
        for word in wordlist:
            perfect.add(word)
            capital[word.lower()].append(word)
            vowel[to_vowel(word)].append(word)
            
        res = []
        for word in queries:
            tmp = to_vowel(word)
            if word in perfect: res.append(word)
            elif word.lower() in capital: res.append(capital[word.lower()][0])
            elif tmp in vowel: res.append(vowel[tmp][0])
            else: res.append('')
                
        return res