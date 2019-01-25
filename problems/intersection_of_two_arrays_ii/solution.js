/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
  var dic = {};
  var output = [];
  
  for (var i = 0; i < nums1.length; i++) {
    if (dic[nums1[i]] === undefined) dic[nums1[i]] = 1;
    else dic[nums1[i]]++;
  }
  
  for (var j = 0; j < nums2.length; j++) {
    if (dic[nums2[j]] !== undefined) {
      output.push(nums2[j]);
      dic[nums2[j]]--;
      if (dic[nums2[j]] === 0) delete dic[nums2[j]];
    }
  }
  return output;
};