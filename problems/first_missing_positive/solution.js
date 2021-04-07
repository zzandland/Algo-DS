/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const N = nums.length;
    for (let i = 0; i < N; ++i) {
        while (nums[i] > 0 && nums[i] <= N && nums[nums[i] - 1] != nums[i]) {
            let tmp = nums[i];
            nums[i] = nums[nums[i] - 1];
            nums[tmp - 1] = tmp;
        }
    }
    
    for (let i = 0; i < N; ++i) {
        if (nums[i] != i + 1) return i + 1;
    }
    return N + 1;
};