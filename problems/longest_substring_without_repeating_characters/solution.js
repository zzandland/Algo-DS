/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  var max = 0;
  var set = new Set();
  var orderArr = [];
  for (var i = 0; i < s.length; i++) {
    if (set.has(s[i])) {
      if (max < orderArr.length) {
        max = orderArr.length;
      }
      while (orderArr[0] !== s[i]) {
        var toRemove = orderArr.shift();
        set.delete(toRemove);
      }
      orderArr.shift();
      orderArr.push(s[i]);
    } else {
      set.add(s[i]);
      orderArr.push(s[i]);
    }
  }
  return max < orderArr.length ? orderArr.length : max
};