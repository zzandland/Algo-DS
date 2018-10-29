/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  var mid, output;
  var left = 0;
  var right = nums.length - 1;
  while(left !== right) {
    mid = Math.ceil((left + right) / 2);
    if (nums[mid] === target) {
      return mid;
    }
    if (nums[mid] > target) {
      right = mid - 1;
    } 
    if (nums[mid] < target) {
      left = mid;
    }
  }
  return nums[0] === target ? 0 : -1
};