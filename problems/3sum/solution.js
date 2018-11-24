/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var binarySort = function(arr) {
  var sorted = [arr[0]];
  var left, right;
  for (var i = 1; i < arr.length; i++) {
    left = 0;
    right = sorted.length - 1;
    var found = false;
    while (right > left && !found) {
      var mid = left + Math.floor((right - left) / 2);
      if (sorted[mid] === arr[i]) {
        sorted.splice(mid, 0, arr[i]);
        found = true;
      } else if (sorted[mid] > arr[i]) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    if (!found) {
      if (sorted[left] > arr[i]) {
        sorted.splice(left, 0, arr[i]);
      } else {
        sorted.splice(left + 1, 0, arr[i]);
      }
    }
  }
  return sorted;  
}

var threeSum = function(nums) {
  if (nums.length < 3) {
    return [];
  }
  var output = [];
  var cuts = [];
  var dic = {};
  var set = new Set();
  for (var i = 0; i < nums.length; i++) {
    if (!dic[nums[i]]) {
      dic[nums[i]] = 1;
    } else {
      dic[nums[i]] += 1;
    }
  }
  for (var num in dic) {
    var occur;
    if (dic[num] > 3) {
      occur = 3;
    } else {
      occur = dic[num];
    }
    while (occur > 0) {
      cuts.push(parseInt(num, 10));
      occur--;
    }
  }
  var sorted = binarySort(cuts);
  for (var j = 0; j < sorted.length; j++) {
    var target = 0 - sorted[j];
    var without = sorted.slice(0, j).concat(sorted.slice(j + 1));
    var left = 0; 
    var right = without.length - 1;
    while (right > left) {
      var sum = without[left] + without[right];
      if (sum === target) {
        var subArr = binarySort([without[left], without[right], sorted[j]]);
        if (!set.has(subArr.join(''))) {
          output.push(subArr);
          set.add(subArr.join(''));
        }
        right--;
      } else if (sum > target) {
        right--;
      } else {
        left++;
      }
    }
  }
  return output;
};