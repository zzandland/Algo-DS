/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
  var left = 0;
  var right = nums.length - 1;
  var mid
  if (nums[left] > nums[right]) {
    while (right > left) {
      mid = left + Math.floor((right - left) / 2);
      if (nums[left] < nums[right]) {
        return nums[left];
      }
      if (nums[mid] >= nums[left]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
  }

  return nums[left];
};