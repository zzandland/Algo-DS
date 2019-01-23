/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
  if (nums === null || nums.length === 0) return [-1, -1];
  let left = 0;
  let right = nums.length - 1;
  while (right > left + 1) {
    let mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) {
      let i, j;
      i = j = mid;
      while (nums[i] === target) { i++; }
      while (nums[j] === target) { j--; }
      return [j + 1, i - 1];
    }
    if (nums[mid] > target) right = mid;
    else left = mid;  
  }
  if (nums[left] === target && nums[right] === target) return [left, right];
  if (nums[left] === target) return [left, left];
  if (nums[right] === target) return [right, right];
  return [-1, -1];
};