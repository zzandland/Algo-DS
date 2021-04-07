/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    res = [];
    for (let i = 0; i < nums.length - 2; ++i) {
        if (i > 0 && nums[i] == nums[i-1]) continue;
        let l = i + 1, r = nums.length - 1, t = -nums[i];
        while (l < r) {
            let t2 = nums[l] + nums[r];
            if (t2 === t) {
                res.push([-t, nums[l++], nums[r]]);  
                while (l < r && nums[l] === nums[l-1]) ++l;
            } else if (t2 >= t) {
                --r;  
            } else {
                ++l;  
            } 
        }
    }
    return res;
};