from collections import OrderedDict, defaultdict

class LFUCache:
    
    def __init__(self, capacity: int):
        self.dicts = defaultdict(OrderedDict)
        self.freq = {}
        self.min = 1
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.freq: return -1
        freq = self.freq[key]
        prev = self.dicts[freq]
        val = prev[key]
        del prev[key]
        if freq == self.min and not prev: self.min += 1
        self.dicts[freq+1][key] = val
        self.freq[key] = freq+1
        return val
        
    def put(self, key: int, value: int) -> None:
        if not self.cap: return
        if key in self.freq:
            self.get(key)
            self.dicts[self.freq[key]][key] = value
        else:
            if len(self.freq) == self.cap:
                out = self.dicts[self.min].popitem(last=False)
                del self.freq[out[0]]
            self.min = 1
            self.dicts[self.min][key] = value
            self.freq[key] = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)