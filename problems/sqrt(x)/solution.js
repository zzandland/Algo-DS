/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
  var left = 0;
  var right = x;
  var mid;
  while (right > left) {
    mid = left + Math.floor((right - left) / 2);
    if (mid * mid <= x && (mid + 1) * (mid + 1) > x) return mid;
    if (mid * mid > x) right = mid;
    else left = mid + 1;
  }
  return left;
};