/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const split = s.split('');
    const dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 2,
        'IX': 2,
        'XL': 20,
        'XC': 20,
        'CD': 200,
        'CM': 200,
    };
    let res = 0;
    for (let c of split) res += (dic[c] === undefined ? 0 : dic[c]);
    for (let i = 0; i < split.length - 1; ++i) {
        let ss = split[i] + split[i+1];
        res -= (dic[ss] === undefined ? 0 : dic[ss]);
    }
    return res;
};