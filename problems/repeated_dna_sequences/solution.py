class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # bitmap -> only possible combs are A, T, C, G: assign a bit to them
        # A -> 00 T -> 01 C -> 10 G -> 11
        # iterate and add code at index
        bm = 0
        dic = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
        seen = set()
        res = set()
        for i in range(len(s)):
            # if i is greater than 10, we need to erase the higher bits
            if i >= 10:
                bm &= ~(3 << 20)
                if bm in seen: res.add(s[i-10:i])
                seen.add(bm)
            bm <<= 2
            bm |= dic[s[i]]
        bm &= ~(3 << 20)
        if bm in seen: res.add(s[i-9:i+1])
        return list(res)