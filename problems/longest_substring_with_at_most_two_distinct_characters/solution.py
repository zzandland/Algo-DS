class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        head = tail = max_len = cnt = 0
        c_map = [0] * 256
        while tail < len(s):
            c_index = ord(s[tail])
            if c_map[c_index] == 0:
                cnt += 1
            c_map[c_index] += 1    
            tail += 1
            while cnt > 2:
                c_index = ord(s[head])
                c_map[c_index] -= 1
                if c_map[c_index] == 0:
                    cnt -= 1
                head += 1    
            if tail - head > max_len:
                max_len = tail - head    
        return max_len