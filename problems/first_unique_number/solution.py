class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = OrderedDict()
        self.dup = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if not self.unique: return -1
        return next(iter(self.unique.items()))[0]

    def add(self, value: int) -> None:
        if value in self.unique:
            self.unique.pop(value)
            self.dup.add(value)
        elif value not in self.dup:
            self.unique[value] = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)