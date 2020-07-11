import bisect
from collections import defaultdict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.dic[key]
        if not vals: return ''
        idx = bisect.bisect(vals, (timestamp,))
        if idx == 0 and vals[0][0] > timestamp: return ''
        if idx == len(vals) or vals[idx][0] > timestamp: return vals[idx-1][1]
        return vals[idx][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)