/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let res = 0;
    const INT_MAX = Math.floor((Math.pow(2, 31) - 1) / 10);
    const INT_MIN = Math.ceil(Math.pow(2, 31) / -10);
    while (x != 0) {
        let pop = x % 10;
        x = x > 0 ? Math.floor(x / 10) : Math.ceil(x / 10);
        if (res > INT_MAX || (res == INT_MAX && pop > 7)) return 0;
        if (res < INT_MIN || (res == INT_MIN && pop < -8)) return 0;
        res = res * 10 + pop;
    }
    return res;
};