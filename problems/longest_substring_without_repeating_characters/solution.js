/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const st = new Set();
    let res = 0;
    for (let i = 0, j = 0; i < s.length; ++i) {
        while (st.has(s[i])) st.delete(s[j++]);
        st.add(s[i]);
        if (i - j + 1 > res) res = i - j + 1;
    }
    return res;
};