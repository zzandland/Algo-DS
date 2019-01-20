/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
  var regex = /^\s*[-+]?\d+/;
  if (!regex.exec(str)) return 0;
  var num = parseInt(regex.exec(str)[0]);
  if (num > Math.pow(2, 31) - 1) return Math.pow(2, 31) - 1;
  if (num < Math.pow(2, 31) * -1) return Math.pow(2, 31) * -1;
  return num;
};
