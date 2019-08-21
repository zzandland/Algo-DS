class Solution {
public:
  vector<vector<int>> permute(vector<int>& nums) {
    if (nums.size() == 0) {
      vector<vector<int>> out;
      out.push_back(vector<int>());
      return out;
    }
    return recurse(nums);
  }
  
  vector<vector<int>> recurse(vector<int>& nums) {
    vector<vector<int>> output;
    if (nums.size() == 1) {
      vector<int> single = {nums[0]};
      output.push_back(single);
      return output;
    }
    int out = nums[nums.size()-1];
    nums.pop_back();
    vector<vector<int>> prev = recurse(nums);
    for (int i = 0; i < prev.size(); ++i) {
      for (int j = 0; j <= prev[i].size(); ++j) {
        vector<int> tmp = prev[i];
        tmp.insert(tmp.begin()+j, out);
        output.push_back(tmp);
      }
    }
    return output;
  }
};