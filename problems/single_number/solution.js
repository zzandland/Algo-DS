/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  var set = new Set();
  var num;
  for (var i = 0; i < nums.length; i++) {
    if (set.has(nums[i])) {
      set.delete(nums[i]);
    } else {
      set.add(nums[i]);
    }
  }
  return set.values().next().value;
};