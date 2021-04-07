/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    const N = s.length;
    let dp = Array.from(Array(N), () => new Array(N).fill(false));
    for (let i = 0; i < N; ++i) {
        dp[i][i] = true;
        if (i > 0) dp[i][i-1] = true;
    }
    let i, j;
    i = j = 0;
    for (let y = N-1; y >= 0; --y) {
        for (let x = y + 1; x < N; ++x) {
            if (s[x] === s[y] && dp[y+1][x-1]) {
                if (x - y > i - j) {
                    i = x;
                    j = y;
                }
                dp[y][x] = true;
            }
        }
    }
    return s.substring(j, i+1);
};