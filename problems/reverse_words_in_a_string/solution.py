class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words) // 2):
            words[i], words[-1 - i] = words[-1 - i], words[i]
        return ' '.join(words).strip()