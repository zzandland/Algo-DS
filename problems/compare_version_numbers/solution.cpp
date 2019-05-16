class Solution {
public:
  vector<int> getArr(string version) {
    vector<int> out;
    int curr = 0, prev = 0;
    curr = version.find('.');
    while (curr != string::npos) {
      out.push_back(stoi(version.substr(prev, curr - prev)));
      prev = curr + 1;
      curr = version.find('.', prev);
    }
    out.push_back(stoi(version.substr(prev)));
    return out;
  }  

  int compareVersion(string version1, string version2) {
    vector<int> v1_arr = getArr(version1);
    vector<int> v2_arr = getArr(version2);
    
    for (int i = 0; i < v1_arr.size() || i < v2_arr.size(); ++i) {
      int num1, num2;
      num1 = (i >= v1_arr.size()) ? 0 : v1_arr[i];
      num2 = (i >= v2_arr.size()) ? 0 : v2_arr[i];
      if (num1 != num2) return num1 > num2 ? 1 : -1;
    }
    return 0;
  }
};