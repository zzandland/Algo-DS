from typing import Tuple

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if not S or not words: return 0
        def compress(s: str) -> List[Tuple[str, int]]:
            output, c1, cnt = [], s[0], 0
            for c2 in s:
                if c1 == c2: cnt += 1
                else: 
                    output.append((c1, cnt))
                    cnt = 1
                c1 = c2    
            output.append((c1, cnt))    
            return output    
        sc = compress(S)
        output = 0
        for word in words:
            if not word: continue
            wc = compress(word)
            if len(sc) == len(wc):
                gud = True
                for i in range(len(sc)):
                    sl, scnt = sc[i]
                    wl, wcnt = wc[i]
                    if sl != wl or wcnt > scnt or (scnt < 3 and wcnt != scnt): 
                        gud = False
                        break
                if gud: output += 1
        return output            