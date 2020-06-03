class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        S, vowels = len(s), set(['a', 'e', 'i', 'o', 'u'])
        run = res = sum([1 for c in s[:k] if c in vowels]) 
        for i in range(k, S):
            if s[i] in vowels: run += 1    
            if s[i-k] in vowels: run -= 1
            res = max(res, run)
        return res