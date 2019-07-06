from typing import Tuple

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if len(S) == 0 or len(words) == 0:
            return 0
        S_g = self.get_counts(S)    
        output = 0
        for word in words:
            w_g = self.get_counts(word)
            if len(S_g) != len(w_g):
                continue
            match = True
            for i, S_ in enumerate(S_g):
                w_ = w_g[i]
                if S_[0] != w_[0] or S_[1] < w_[1]:
                    match = False
                    break
                if S_[1] == 1 or S_[1] == 2:
                    if w_[1] != S_[1]:
                        match = False
                        break
            if match:
                output += 1
        return output        
                            
    def get_counts(self, S: str) -> List[Tuple[str, int]]:
        output = []
        prev, cnt = S[0], 1
        for i in range(1, len(S)):
            if S[i] == prev:
                cnt += 1
            else:
                output.append((prev, cnt))    
                prev, cnt = S[i], 1
        output.append((prev, cnt))        
        return output