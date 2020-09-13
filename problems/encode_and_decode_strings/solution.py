class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ln = map(str, map(len, strs))
        return '%s/////%s' % (','.join(list(ln)), ''.join(strs))

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == '/////': return []
        ln, strs = s.split('/////')
        i = 0
        res = []
        for l in ln.split(','):
            l = int(l)
            res.append(strs[i:i+l])
            i += l
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))