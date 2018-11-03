/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  var minHeight, area;
  var left = 0; 
  var right = height.length - 1;
  var maxArea = 0;
  while (right > left) {
    minHeight = Math.min(height[left], height[right]);
    area = minHeight * (right - left);
    if (area > maxArea) {
      maxArea = area;
    }
    if (height[right] >= height[left]) {
      left++;
    } else {
      right--;
    }
  }
  return maxArea;
};