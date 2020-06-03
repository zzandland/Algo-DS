class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        S = len(searchWord)
        for i, word in enumerate(sentence.split()):
            if word[:S] == searchWord: return i+1
        return -1