/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let a = 0, b = 0;
    for (const n of nums) {
        if (n > a) {
            b = a;
            a = n;
        } else if (n > b) {
            b = n;
        }
    }
    return (a-1) * (b-1);
};