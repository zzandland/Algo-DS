/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    let pos = n > 0;
    if (!pos) n = Math.abs(n);
    let res = 1;
    let st = [[1, x]];
    while (st[st.length-1][0]*2 < n) {
        st.push([st[st.length-1][0]*2, st[st.length-1][1] * st[st.length-1][1]])
    }
    while (n > 0) {
        while (st[st.length-1][0] > n) st.pop();
        res *= st[st.length-1][1];
        n -= st[st.length-1][0];
    }
    return pos ? res : 1 / res;
};