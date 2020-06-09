class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = [homepage]
        self.fwd = []

    def visit(self, url: str) -> None:
        self.prev.append(url)
        self.fwd = []

    def back(self, steps: int) -> str:
        while len(self.prev) > 1 and steps > 0:
            self.fwd.append(self.prev.pop())
            steps -= 1
        return self.prev[-1]

    def forward(self, steps: int) -> str:
        while self.fwd and steps > 0:
            self.prev.append(self.fwd.pop())
            steps -= 1
        return self.prev[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)