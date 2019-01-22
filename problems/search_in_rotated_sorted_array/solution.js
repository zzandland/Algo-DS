/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  if (nums === null || nums.length === 0) return -1;
  var left = 0;
  var right = nums.length - 1;
  var pivot = findPivot(nums);
  if (nums[right] >= target) return binarySearch(nums, pivot, right, target);
  else return binarySearch(nums, 0, pivot - 1, target);
};

function findPivot(nums) {
  var left = 0;
  var right = nums.length - 1;
  if (nums[left] < nums[right] || left === right) return 0;
  while (right > left + 1) {
    var mid = left + Math.floor((right - left) / 2);
    if (mid + 1 < nums.length && nums[mid] > nums[mid + 1]) return mid + 1;
    if (mid - 1 >= 0 && nums[mid - 1] > nums[mid]) return mid;
    if (nums[mid] < nums[right]) right = mid;
    else left = mid;
  }
  return right;
}

function binarySearch(nums, left, right, target) {
  while (right >= left) {
    var mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) return mid;
    if (nums[mid] > target) right = mid - 1;
    else left = mid + 1;
  }
  return -1;
}