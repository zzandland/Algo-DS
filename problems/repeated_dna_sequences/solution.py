class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
        bitmask, seen, res = 0, set(), set()
        for i in range(len(s)+1):
            if i >= 10:
                if bitmask in seen:
                    res.add(s[i-10:i])
                seen.add(bitmask)    
            if i < len(s):
                bitmask <<= 2
                bitmask |= dic[s[i]]
                bitmask &= ~(3 << 2*10)
        return res