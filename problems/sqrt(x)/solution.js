/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let l = 1, r = x;
    while (l < r) {
        let m = l + Math.floor((r - l) / 2);
        console.log(m)
        if (m * m === x) return m;
        if (m * m < x) l = m + 1;
        else r = m;
    }
    return l * l <= x ? l : l - 1;
};