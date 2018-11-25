/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  var output = [];
  var temp;
  var sorted;
  for (var i = 0; i < nums.length; i++) {
    sorted = true;
    for (var j = 0; j < nums.length - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        temp = nums[j + 1];
        nums[j + 1] = nums[j];
        nums[j] = temp;
        sorted = false;
      }
    }
    if (sorted) break;
  }
  var target, left, right, sum, subArr;
  for (var j = 0; j < nums.length - 2; j++) {
    if (nums[j] === nums[j - 1] && j < nums.length - 2) {
      continue;
    }
    target = 0 - nums[j];
    left = j + 1; 
    right = nums.length - 1;
    while (right > left) {
      if (nums[left] === nums[left - 1] && left < nums.length - 1 && left - 1 !== j) {
        left++;
        continue;
      }
      if (nums[right] === nums[right + 1] && right > left) {
        right--;
        continue;
      }
      sum = nums[left] + nums[right];
      if (sum === target) {
        subArr = [nums[j], nums[left], nums[right]];
        output.push(subArr);
        left++;
      } else if (sum > target) {
        right--;
      } else {
        left++;
      }
    }
  }
  return output;
};