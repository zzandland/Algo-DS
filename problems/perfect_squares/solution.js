/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
  var round = 1;
  var perfectSquares = [];
  var set = new Set();
  for (var i = 1; (i * i) <= n; i++) {
    perfectSquares.push(i * i);
    set.add(i * i);
  }
  var queue = [...perfectSquares]
  if (n === perfectSquares[perfectSquares.length - 1]) {
    return 1;
  }
  var val, length, sum;
  while (queue.length) {
    round++;
    length = queue.length;
    for (var j = 0; j < length; j++) {
      val = queue.pop();
      for (var k = 0; k < perfectSquares.length; k++) {
        sum = val + perfectSquares[k];
        if (sum === n) {
          return round;
        } else if (sum < n && !set.has(sum)) {
          set.add(sum);
          queue.unshift(sum);
        } else if (sum > n) {
          break;
        }
      }
    }
  }
  return 0;
};