/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    const vowels = new Set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']);
    let a, b;
    a = b = 0;
    for (let i = 0; i < s.length / 2; ++i) {
        if (vowels.has(s[i])) ++a;
        if (vowels.has(s[s.length / 2 + i])) ++b;
    }
    return a === b;
};