/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var i = 1;
    var res = [];
    while (i <= n) {
        if (i % 3 === 0 && i % 5 === 0) {
            res.push('FizzBuzz');
        } else if (i % 3 === 0) {
            res.push('Fizz');
        } else if (i % 5 === 0) {
            res.push('Buzz');
        } else {
            res.push(i.toString());
        }
        i += 1;
    }
    return res;
};