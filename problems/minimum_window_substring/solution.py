class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N, M = len(s), len(t)
        if M > N or M == 0 or N == 0:
            return ""
        letters = [0] * 256
        for c in t:
            letters[ord(c)] += 1
        end, start, count, min_start, min_len = 0, 0, M, 0, float('inf')    
        while end < N:
            letters[ord(s[end])] -= 1
            if letters[ord(s[end])] >= 0:
                count -= 1
            end += 1    
            while count == 0:
                if end - start < min_len:
                    min_start = start
                    min_len = end - start
                letters[ord(s[start])] += 1    
                if letters[ord(s[start])] > 0:
                    count += 1
                start += 1    
        if min_len == float('inf'):
            return ""        
        else:
            return s[min_start:min_start + min_len]    