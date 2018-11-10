/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
  var set = new Set();
  var num = n;
  var numArr;
  while (num !== 1) {
    numArr = num.toString().split('');
    num = numArr.map(digit => Math.pow(parseInt(digit, 10), 2)).reduce((a, b) => a + b);   
    if (set.has(num)) {
      return false;
    }
    set.add(num)
  }
  return true;
};