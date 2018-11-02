/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  if (nums.length === 1) {
    return nums[0] === target ? 0 : -1
  }
  var left, right, mid, leftDif, rightDif, max;
  left = 0;
  right = nums.length - 1;
  if (nums[left] < nums[right]) {
    max = right;
  }
  while (right > left && max === undefined) {
    mid = left + Math.floor((right - left) / 2);
    if (nums[mid] > nums[mid + 1]) {
      max = mid;
      break;
    }
    leftDif = Math.abs(nums[mid] - nums[left]);
    rightDif = Math.abs(nums[mid] - nums[right]);
    if (leftDif > rightDif) {
      right = mid;
    } else if (leftDif < rightDif) {
      left = mid;
    }
  }
  if (max === undefined) {
    max = left - 1;
  }
  
  if (target >= nums[0]) {
    left = 0;
    right = max;
  } else if (target < nums[0]) {
    left = max + 1;
    right = nums.length - 1;
  }

  while (right >= left) {
    mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) {
      return mid;
    }
    if (nums[mid] < target) {
      left = mid + 1;
    } else if (nums[mid] > target) {
      right = mid - 1;
    }
  }
  return -1;
};