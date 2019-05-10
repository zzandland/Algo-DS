class Solution {
public:
  int maxArea(vector<int>& height) {
    if (height.size() < 2) return 0;
    int max_area, l, r;
    max_area = 0; l = 0; r = height.size() - 1;
    while (r > l) {
      max_area = max(max_area, (r - l) * min(height[l], height[r]));
      if (height[l] > height[r])
        --r;
      else
        ++l;
    }
    return max_area;
    // if (height.size() < 2) return 0;
    // return maxArea(height, 0, height.size() - 1);
  }
  
  int maxArea(vector<int>& height, size_t l, size_t r) {
    int l_height = height[l];
    int r_height = height[r];
    int area = (r - l) * min(l_height, r_height);
    if (r <= l) return area;
    
    if (l_height == r_height)
      return max(area, max(maxArea(height, l + 1, r), maxArea(height, l, r - 1)));  
    else if (l_height > r_height)
      return max(area, maxArea(height, l, r - 1));
    else 
      return max(area, maxArea(height, l + 1, r));
  }
};