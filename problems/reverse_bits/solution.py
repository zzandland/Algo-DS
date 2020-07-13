class Solution:
    def __init__(self):    
        self.mem = {}

    @staticmethod
    def reverseByte(byte: int) -> int:
        res = 0
        for _ in range(7):
            if byte & 1 == 1: res ^= 1
            res <<= 1
            byte >>= 1
        if byte & 1 == 1: res ^= 1
        return res

    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(3):
            byte = n & 0xff
            if byte not in self.mem: self.mem[byte] = self.reverseByte(byte)
            res ^= self.mem[byte]
            res <<= 8
            n >>= 8
        byte = n & 0xff
        if byte not in self.mem: self.mem[byte] = self.reverseByte(byte)
        res ^= self.mem[byte]
        return res