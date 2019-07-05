class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = tail = 0
        dup, dic = False, [0] * 128
        max_len = 0
        while tail < len(s):
            if dic[ord(s[tail])] == 1:
                dup = True
            dic[ord(s[tail])] += 1    
            tail += 1    
            while dup:
                dic[ord(s[head])] -= 1
                if dic[ord(s[head])] == 1:
                    dup = False
                head += 1    
            max_len = max(max_len, tail - head)    
        return max_len    