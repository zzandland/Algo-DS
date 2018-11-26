/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
  if (digits.length === 0) {
    return [];
  }
  var dic = {};
  var three;
  var charCode = 97;
  for (var i = 2; i < 10; i++) {
    dic[i] = [];
    if (i === 7 || i === 9) {
      three = charCode + 4;
    } else {
      three = charCode + 3;
    }
    while (charCode < three) {
      dic[i].push(String.fromCharCode(charCode));
      charCode++;
    }
  }
  var output = [];
  var num;
  var innerFunc = function(index, arr) {
    if (!arr) {
      arr = [];
    }
    if (index === digits.length) {
      output.push(arr.join(''));
      return;
    }
    num = digits.charAt(index);
    if (num < 2 && num > 9) {
      throw Error("invalid number at index: " + index);
    }
    var comb = dic[num];
    for (var i = 0; i < comb.length; i++) {
      arr.push(comb[i]);
      innerFunc(index + 1, arr);
      arr.pop();
    }
  }
  innerFunc(0);
  return output;
};