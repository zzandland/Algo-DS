/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const obj = {};
    for (const str of strs) {
        const sorted = str.split('').sort().join('');
        if (!obj.hasOwnProperty(sorted)) obj[sorted] = [];
        obj[sorted].push(str);
    }
    return Object.values(obj);
};