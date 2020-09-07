class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic = {}
        seen = {}
        split = str.split()
        if len(pattern) != len(split): return False
        for i, word in zip(pattern, split):
            if word in seen and seen[word] != i: return False
            if i not in dic:
                dic[i] = word
                seen[word] = i
            elif word != dic[i]: return False
        return True