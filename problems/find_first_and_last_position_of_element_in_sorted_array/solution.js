/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    var N = nums.length;
    var bs = function(t) {
        let l = 0, r = N;
        while (l < r) {
            var m = l + Math.floor((r-l) / 2);
            if (nums[m] < t) l = m+1;
            else r = m;
        }
        return l;
    }
    l = bs(target);
    if (l == N || nums[l] != target) return [-1, -1];
    return [l, bs(target+1)-1];
};