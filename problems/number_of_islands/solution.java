class Solution {
  public int numIslands(char[][] grid) {
    int count = 0;
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[0].length; j++) {
        if (grid[i][j] == '1') {
          count++;
          helper(grid, i, j);
        }
      }
    }
    return count;
  }
  
  private void helper(char[][] grid, int x, int y) {
    if (grid[x][y] == '0') return;
    grid[x][y] = '0';
    if (x - 1 >= 0) helper(grid, x - 1, y);
    if (x + 1 < grid.length) helper(grid, x + 1, y);
    if (y - 1 >= 0) helper(grid, x, y - 1);
    if (y + 1 < grid[0].length) helper(grid, x, y + 1);
  }
}
