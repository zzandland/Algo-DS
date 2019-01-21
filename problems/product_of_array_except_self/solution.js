/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  const output = new Array(nums.length).fill(1);
  for (let i = 1; i < nums.length; i++) {
    output[i] = nums[i - 1] * output[i - 1];
  }
  let right = 1;
  for (let j = output.length - 2; j >= 0; j--) {
    right *= nums[j + 1];
    output[j] *= right;
  }
  return output;
};