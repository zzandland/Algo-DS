class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, st = self.check[id]
        del self.check[id]
        self.times[(start, stationName)].append(t-st)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tmp = self.times[(startStation, endStation)]
        return sum(tmp) / len(tmp)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)