/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
  if (nums.length === 1) {
    return nums[0];
  }
  var left = 0;
  var right = nums.length - 1;
  var mid, leftDif, rightDif;
  if (nums[left] < nums[right]) {
    return nums[left];
  }
  while (right > left) {
    mid = left + Math.floor((right - left) / 2);
    if (nums[mid] > nums[mid + 1]) {
      return nums[mid + 1];
    }
    leftDif = Math.abs(nums[mid] - nums[left]);
    rightDif = Math.abs(nums[mid] - nums[right]);
    if (leftDif > rightDif) {
      right = mid;
    } else if (leftDif < rightDif) {
      left = mid;
    }
  }
  return nums[left];
};