/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    res = []
    let a, b;
    a = b = -1;
    intervals.forEach(([s, e]) => {
        if (b < s) {
            res.push([a, b]);
            a = s;
            b = e;
        } else {
            b = Math.max(b, e);
        }
    })
    res.push([a, b]);
    res.shift();
    return res;
};