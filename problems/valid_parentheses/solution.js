/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    st = [];
    for (const c of s) {
        if (c === ')') {
            if (!st.length || st.pop() !== '(') return false;
        } else if (c === ']') {
            if (!st.length || st.pop() !== '[') return false;
        } else if (c === '}') {
            if (!st.length || st.pop() !== '{') return false;
        } else {
            st.push(c);
        }
    }
    return st.length === 0;
};