from collections import Counter

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.seen = Counter()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.seen[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for v in self.seen:
            if v+v == value:
                if self.seen[v] > 1: return True
            elif self.seen[value - v] > 0: return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)