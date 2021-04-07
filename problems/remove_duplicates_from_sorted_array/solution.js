/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0;
    for (let j = 0; j < nums.length; ++i, ++j) {
        while (j > 0 && j < nums.length && nums[j] === nums[j-1]) ++j;
        if (j == nums.length) break;
        nums[i] = nums[j];
    }
    return i;
};