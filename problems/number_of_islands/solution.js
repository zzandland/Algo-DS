/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === '1') {
        count++;
        helper(grid, i, j); 
      }
    } 
  }
  return count;
};

function helper(grid, x, y) {
  if (!grid[x] || !grid[x][y] || grid[x][y] === '0') return;
  grid[x][y] = '0';
  helper(grid, x - 1, y);
  helper(grid, x + 1, y);
  helper(grid, x, y - 1);
  helper(grid, x, y + 1);
}