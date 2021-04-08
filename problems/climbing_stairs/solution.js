/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n < 2) return n;
    let a = 1, b = 1, c;
    for (let i = 2; i <= n; ++i) {
        c = a + b;
        a = b;
        b = c;
    }
    return c;
};