class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    hor, ver = set(), set()
    for r, row in enumerate(matrix):
      for c, col in enumerate(row):
        if col == 0:
          hor.add(c)
          ver.add(r)
    for r, row in enumerate(matrix):
      for c, col in enumerate(row):
        if r in ver or c in hor:
          matrix[r][c] = 0