class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0, 1, 0]
        while rowIndex > 0:
            nrow = [0]
            for a, b in zip(row, row[1:]):
                nrow.append(a+b)
            nrow.append(0)
            row = nrow
            rowIndex -= 1
        return row[1:-1]