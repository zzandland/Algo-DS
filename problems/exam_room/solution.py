import bisect

class ExamRoom:
    def __init__(self, N: int):
        self.N = N
        self.seats = []

    def seat(self) -> int:
        N, seats = self.N, self.seats
        if not seats: idx = 0
        else:
            d, idx = seats[0], 0
            for i in range(len(seats)-1):
                a, b = seats[i], seats[i+1]
                if (b - a) // 2 > d:
                    d, idx = (b - a) // 2, (b + a) // 2
            if N-1 - seats[-1] > d: idx = N-1
        bisect.insort(self.seats, idx)
        return idx

    def leave(self, p: int) -> None:
        self.seats.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)