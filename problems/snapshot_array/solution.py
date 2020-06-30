import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.record = [[(0, 0)] for _ in range(length)]
        self.id = 0

    def set(self, index: int, val: int) -> None:
        self.record[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.record[index]
        l, r = 0, len(snaps)
        while l < r:
            m = l + (r-l)//2
            if snaps[m][0] < snap_id+1: l = m+1
            else: r = m
        return self.record[index][l-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)