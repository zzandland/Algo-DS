/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
  var output = '';
  
  var numArr = num.toString().split('').reverse();
  
  output += helper(numArr[0], 1);
  num = Math.floor(num / 10) * 10;
  
  if (num >= 10) {
    output = helper(numArr[1], 10) + output;
    num = Math.floor(num / 10) * 10;
  }
  if (num >= 100) {
    output = helper(numArr[2], 100) + output;
    num = Math.floor(num / 10) * 10;
  }
  if (num >= 1000) {
    output = helper(numArr[3], 1000) + output;
    num = Math.floor(num / 10) * 10;
  }
  
  return output;
};

var helper = function(num, digits) {
  var digit = parseInt(num, 10);
  if (digit === 4) {
    return dic[digits][1] + dic[digits][5];
  } else if (digit === 9) {
    return dic[digits][1] + dic[digits * 10][1];
  } else {
    var str = '';
    while (digit > 0) {
      if (digit >= 5) {
        str += dic[digits][5];
        digit -= 5;
      } else {
        str += dic[digits][1];
        digit -= 1;
      }
    }
    return str;
  }
}

var dic = {
  1000: {
    1: 'M',
  },
  100: {
    5: 'D',
    1: 'C',
  },
  10: {
    5: 'L',
    1: 'X',
  },
  1: {
    5: 'V',
    1: 'I',
  }
}
