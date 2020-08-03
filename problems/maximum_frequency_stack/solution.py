class FreqStack:
    def __init__(self):
        self.freqs = Counter()
        self.m = defaultdict(list)
        self.mx = 0

    def push(self, x: int) -> None:
        self.freqs[x] += 1
        self.mx = max(self.mx, self.freqs[x])
        self.m[self.freqs[x]].append(x)

    def pop(self) -> int:
        x = self.m[self.mx].pop()
        self.freqs[x] -= 1
        if not self.m[self.mx]: self.mx -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()