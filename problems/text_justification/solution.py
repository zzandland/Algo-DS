class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def calMinWidth(lst: List[str]) -> int:
            return len(''.join(lst)) + len(lst)-1 if len(lst) else 0
        
        def genPad(lst: List[str]) -> List[int]:
            if len(lst) > 1:
                div,mod = divmod(maxWidth - len(''.join(lst)), len(lst)-1)
                return [div+1 for i in range(mod)] + [div for i in range(len(lst)-mod-1)]
            return []
        
        def stitchWordsWithPads(lst: List[str]) -> str:
            out = []
            pads = genPad(lst)
            for i, wrd in enumerate(lst):
                out.append(wrd)
                if i < len(pads): out.append(' '*pads[i])
            s = ''.join(out)
            return s + ' '*(maxWidth-len(s))
        
        lst, output, i = [], [], 0
        while len(words):
            if calMinWidth(lst) <= maxWidth:
                if calMinWidth(words) <= maxWidth: break
                lst.append(words[i])
                i += 1
            else:
                lst.pop()
                output.append(stitchWordsWithPads(lst))
                words = words[i-1:]
                i = 0
                lst = []
        last = ' '.join(words)
        output.append(last + ' '*(maxWidth-len(last)))
        return output