/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let st = [], res = [];
    const helper = i => {
        if (i < 0 || i > n) return;
        if (st.length === n * 2) {
            if (i === 0) res.push(st.join(''));
            return;
        }
        st.push('(');
        helper(i+1);
        st.pop();
        st.push(')');
        helper(i-1);
        st.pop();
    }
    helper(0);
    return res;
};