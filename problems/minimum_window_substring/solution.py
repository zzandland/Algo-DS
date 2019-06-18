class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_dict = [0] * 256
        for c in t:
            char_dict[ord(c)] += 1
        start, end, min_len, min_start, counter = 0, 0, -1, 0, len(t)
        while end < len(s):
            if char_dict[ord(s[end])] > 0:
                counter -= 1
            char_dict[ord(s[end])] -= 1    
            end += 1
            while counter == 0:
                if min_len == -1 or end - start < min_len:
                    min_start = start
                    min_len = end - start
                char_dict[ord(s[start])] += 1    
                if char_dict[ord(s[start])] > 0:
                    counter += 1    
                start += 1    
        if min_len == -1:
            return ""
        else:
            return s[min_start:min_start + min_len]