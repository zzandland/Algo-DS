/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (!digits) return [];
    const lts = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    let st = [], res = [];
    const helper = i => {
        if (i === digits.length) {
            res.push(st.join(''));
            return;
        }
        for (let c of lts[digits[i]]) {
            st.push(c);
            helper(i+1);
            st.pop();
        }
    }
    helper(0);
    return res;
};