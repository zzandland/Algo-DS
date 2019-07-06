class Solution:
    def minWindow(self, s: str, t: str) -> str:
        head = tail = 0
        c_map, cnt = [0] * 256, len(t)
        min_len,  min_h = float('inf'), 0
        for c in t:
            c_map[ord(c)] += 1
        while tail < len(s):
            c_index = ord(s[tail])
            if c_map[c_index] > 0:
                cnt -= 1
            c_map[c_index] -= 1
            tail += 1
            while cnt == 0:
                if tail - head < min_len:
                    min_len = tail - head
                    min_h = head
                c_index = ord(s[head])    
                if c_map[c_index] == 0:
                    cnt += 1
                c_map[c_index] += 1    
                head += 1
        if min_len == float('inf'):
            return ""
        else: return s[min_h:min_h+min_len]        