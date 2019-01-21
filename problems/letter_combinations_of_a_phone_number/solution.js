/**
 * @param {string} digits
 * @return {string[]}
 */
const numbers = {
  2: ['a', 'b', 'c'],
  3: ['d', 'e', 'f'],
  4: ['g', 'h', 'i'],
  5: ['j', 'k', 'l'],
  6: ['m', 'n', 'o'],
  7: ['p', 'q', 'r', 's'],
  8: ['t', 'u', 'v'],
  9: ['w', 'x', 'y', 'z'],
}

var letterCombinations = function(digits) {
  const output = [];
  if (digits === '') return output;
  helper(output, digits, [], 0);
  return output;
};

function helper(output, digits, arr, index) {
  if (index === digits.length) {
    output.push(arr.join(''));
    return;
  }
  const chars = numbers[digits[index]];
  for (let i = 0; i < chars.length; i++) {
    arr.push(chars[i]);
    index++;
    helper(output, digits, arr, index);
    arr.pop();
    index--;
  }
}