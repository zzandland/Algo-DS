/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let i = 0, j = nums.length - 1;
    while (i < j) {
        if (nums[i] !== val) {
            i++;
        } else {
            nums[i] = nums[j];
            nums[j--] = val;
        }
    }
    return nums[i] === val ? i : i+1;
};