/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    var sqs = [];
    for (var i = 0; i * i <= n; i++) {
      sqs.push(i*i);
    }
    dp = Array(n+1).fill(Infinity);
    dp[0] = 0;
    for (var sq of sqs) {
        for (var i = sq; i < n+1; i++) {
            dp[i] = Math.min(dp[i], dp[i - sq] + 1);
        }
    }
    return dp[n];
};