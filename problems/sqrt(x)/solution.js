/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
  if (x === 0) {
    return 0;
  } else if (x === 1) {
    return 1;
  }
  var left = 1;
  var right = x;
  var mid;
  while (left !== right) {
    mid = Math.floor((left + right) / 2);
    if (mid * mid === x) {
      return mid;
    }
    if (mid * mid < x) {
      left = mid + 1;
    }
    if (mid * mid > x) {
      right = mid;
    }
  }
  return left - 1;
};