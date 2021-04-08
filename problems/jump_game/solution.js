/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let res = 0;
    for (let i = 0; i < nums.length; ++i) {
        if (res < i) return false;
        res = Math.max(res, i + nums[i]);
        if (res >= nums.length) return true;
    }
    return res >= nums.length - 1;
};