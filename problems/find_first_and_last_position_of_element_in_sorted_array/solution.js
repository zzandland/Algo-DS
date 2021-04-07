/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    const bs = (t) => {
        let l = 0, r = nums.length;
        while (l < r) {
            let m = l + Math.floor((r - l) / 2);
            if (nums[m] >= t) r = m;
            else l = m + 1;
        }
        return l;
    }
    let idx = bs(target);
    if (idx == nums.length || nums[idx] != target) return [-1, -1];
    return [bs(target), bs(target+1) - 1];
};