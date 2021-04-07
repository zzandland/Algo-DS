/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    let pos = true;
    if (dividend < 0) {
        pos = !pos;
        dividend = Math.abs(dividend);
    }
    if (divisor < 0) {
        pos = !pos;
        divisor = Math.abs(divisor);
    }
    let st = [[1, divisor]], res = 0;
    while (dividend > st[st.length - 1][1] + st[st.length - 1][1]) {
        let base = st[st.length - 1][0] + st[st.length - 1][0];
        let n = st[st.length - 1][1] + st[st.length - 1][1];
        st.push([base, n]);
    }
    while (dividend >= divisor) {
        res += st[st.length - 1][0];
        dividend -= st[st.length - 1][1];
        while (st.length && dividend < st[st.length - 1][1]) {
            st.pop();
        }
    }
    return pos ? Math.min(Math.pow(2, 31) - 1, res) : res * -1;
};