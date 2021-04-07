/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    const helper = arr => {
        let cur = arr[0], freq = 1, res = [];
        for (let i = 1; i < arr.length; ++i) {
            if (cur != arr[i]) {
                res.push(freq.toString());
                res.push(cur)
                cur = arr[i];
                freq = 1;
            } else {
                ++freq;
            }
        }
        res.push(freq.toString());
        res.push(cur)
        return res;
    }
    arr = ['1'];
    while (--n > 0) {
        arr = helper(arr);
    }
    return arr.join('');
};