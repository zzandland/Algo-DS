/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
  if (nums.length === 1) return 0;
  if (nums.length === 2) return nums.indexOf(Math.max(...nums));
  let left = 0;
  let right = nums.length - 1;
  while (right > left + 1) {
    let mid = left + Math.floor((right - left) / 2);
    if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) return mid;
    if (nums[mid] > nums[mid - 1] && nums[mid + 1] > nums[mid]) left = mid;
    else right = mid;
  }
  if (nums[right] > nums[left]) return right;
  else return left;
};