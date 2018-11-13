/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  var obj = {};
  var diff;
  for (var i = 0; i < nums.length; i++) {
    diff = target - nums[i];
    if (obj[diff] !== undefined) {
      return [obj[diff], i];
    } 
    obj[nums[i]] = i;
  }
};