class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = data[::-1]
        k = 0
        while data:
            byte = data.pop()
            if k == 0:
                if byte < 128: continue
                if byte >= 240:
                    if 1 << 3 & byte != 0: return False
                    k = 3
                elif byte >= 224:
                    if 1 << 4 & byte != 0: return False
                    k = 2
                elif byte >= 192:
                    if 1 << 5 & byte != 0: return False
                    k = 1
                else: return False
            else:
                if (1 << 7) & byte != 128 or (1 << 6) & byte != 0: return False
                k -= 1
        return k == 0