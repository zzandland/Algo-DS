/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    debugger;
  var output = 0;
  var set = new Set();
  var queue;
  var checkIsland = function(x, y) {
    if (!set.has([x, y].toString())) {
      output++;
      queue = [[x, y]];
      var coor;
      while (queue.length) {
          coor = queue.pop();
          var X = coor[0];
          var Y = coor[1];
          set.add(coor.toString());
          if (
            grid[X + 1] 
            && grid[X + 1][Y] === '1'
            && !set.has([X + 1, Y].toString())) {
                set.add([X + 1, Y].toString());
            queue.unshift([X + 1, Y]);
          }
          if (
            grid[X - 1] 
            && grid[X - 1][Y] === '1'
            && !set.has([X - 1, Y].toString())) {
                set.add([X - 1, Y].toString());
            queue.unshift([X - 1, Y]);
          }
          if (
            grid[X][Y + 1] 
            && grid[X][Y + 1] === '1'
            && !set.has([X, Y + 1].toString())) {
                set.add([X, Y + 1].toString());
            queue.unshift([X, Y + 1]);
          }
          if (
            grid[X][Y - 1] 
            && grid[X][Y - 1] === '1'
            && !set.has([X, Y - 1].toString())) {
                set.add([X, Y - 1].toString());
            queue.unshift([X, Y - 1]);
          }    
        
      }
    }
  }
  for (var i = 0; i < grid.length; i++) {
    for (var j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === '1') {
        checkIsland(i, j);
      }
    }
  }
  return output;
};