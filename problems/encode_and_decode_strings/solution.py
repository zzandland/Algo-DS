class Codec:
    def padHex(self, c: int) -> str:    
        res = hex(c)[2:]
        if len(res) < 2: return '0' + res
        return res

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(self.padHex(len(s)))
            for c in s:
                res.append(self.padHex(ord(c)))
        return ''.join(res)
        
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        ln = 0
        tmp = []
        for i in range(0, len(s), 2):
            if ln == 0:
                res.append(''.join(tmp))
                tmp = []
                ln = int(s[i:i+2], 16)
            else: 
                tmp.append(chr(int(s[i:i+2], 16)))
                ln -= 1
        res.append(''.join(tmp))
        return res[1:]
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))