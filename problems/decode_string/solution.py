from typing import Tuple

class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s, 0, 1)[0]
        
    def helper(self, s: str, i: int, k: int) -> Tuple[str, int]:
        buf, output = [], ""
        while i < len(s) and s[i] != ']':
            if s[i].isdigit():
                cnt = ""
                while s[i].isdigit():
                    cnt += s[i]
                    i += 1
                result, i = self.helper(s, i + 1, int(cnt))
                buf.append(result)
            else:
                buf.append(s[i])    
                i += 1
        buf_str = ''.join(buf)
        for _ in range(k):
            output += buf_str
        return (output, i + 1)    