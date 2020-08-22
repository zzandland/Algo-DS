class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic.setdefault(key, [[0, '']])
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_left(self.dic[key], [timestamp+1]) - 1 
        return self.dic[key][idx][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)