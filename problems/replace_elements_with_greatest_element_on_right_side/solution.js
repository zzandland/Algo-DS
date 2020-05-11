/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    mx = -1
    for (let i = arr.length-1; i >= 0; i--) {
      tmp = Math.max(mx, arr[i]);
      arr[i] = mx;
      mx = tmp;
    }
    return arr;
};