/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    return Math.max(...accounts.map(acc => acc.reduce((a, b) => a + b, 0)));
};