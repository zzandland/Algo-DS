/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
      if (n === 1) {
        return 1;
      }
      var left = 1;
      var right = n;
      var mid;
      while (right > left) {
        mid = left + Math.floor((right - left) / 2);
        if (!isBadVersion(mid) && isBadVersion(mid + 1)) {
          return mid + 1;
        }
        if (!isBadVersion(mid)) {
          left = mid + 1;
        } else if (isBadVersion(mid)) {
          right = mid;
        }
      }
      return isBadVersion(left) ? left : -1
    };
};