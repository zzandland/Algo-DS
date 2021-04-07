/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    res = [[]]
    for (const n of nums) {
        let tmp = []
        for (const arr of res) {
            for (let i = 0; i <= arr.length; ++i) {
                tmp.push(arr.slice(0, i).concat([n]).concat(arr.slice(i)));
            }
        }
        res = tmp;
    }
    return res;
};