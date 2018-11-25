/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  var longest = [];
  var grid = [];
  for (var i = 0; i < s.length; i++) {
    grid[i] = [];
  }
  for (var j = 0; j < s.length; j++) {
    for (var k = 0; k < s.length; k++) {
      if (j === 0) {
        grid[k][k] = true;
        longest = [k, k];        
      } else if (j === 1) {
        if (s[k] === s[k + j]) {
          grid[k][k + j] = true;
          longest = [k, k + j];
        }
      } else {
        if (s[k] === s[k + j] && grid[k + 1][k + j - 1]) {
          grid[k][k + j] = true;
          longest = [k, k + j];
        }
      }
    }
  }
  return s.slice(longest[0], longest[1] + 1);
};