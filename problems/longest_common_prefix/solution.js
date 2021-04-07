/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (!strs.length) return '';
    let res = [];
    for (i = 0; i < 200; ++i) {
        if (i >= strs[0].length) return res.join('');
        let p = strs[0][i];
        for (let j = 1; j < strs.length; ++j) {
            if (i >= strs[j].length || strs[j][i] != p) return res.join('');
        }
        res.push(p);
    }
    return res.join('');
};