/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
  var set = new Set();
  var output = [];
  for (var i = 0; i < nums1.length; i++) {
    set.add(nums1[i]);
  }
  for (var j = 0; j < nums2.length; j++) {
    if (set.has(nums2[j])) {
      output.push(nums2[j]);
      set.delete(nums2[j]);
    }
  }
  return output;
};