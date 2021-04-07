/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let i = 0;
    let res = [];
    let neg = false;
    while (s[i] === ' ') ++i;
    if (s[i] === '+' || s[i] === '-') {
        if (s[i] === '-') neg = true;
        ++i;
    }
    while (s[i] >= '0' && s[i] <= '9') {
        res.push(s[i++]);
    }
    if (!res.length) return 0;
    let n = parseInt(res.join(''), 10) * (neg ? -1 : 1);
    if (n >= 0) {
        const MAX = Math.pow(2, 31) - 1;
        return Math.min(MAX, n);
    }
    return Math.max(Math.pow(2, 31) * -1, n);
};