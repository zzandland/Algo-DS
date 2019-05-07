#include <iostream>
#include <map>
#include <vector>

enum class Method { BRUTE, MEM, BU };

int StrInterleaving(std::string str1, std::string str2, std::string target,
                    Method m);
int Brute(std::string str1, std::string str2, std::string target, int i1,
          int i2, int ti);
int Memoize(std::string str1, std::string str2, std::string target, int i1,
            int i2, int ti, std::map<std::string, bool>& dp);
int BU(std::string str1, std::string str2, std::string target);

int main(void) {
  Method m = Method::BU;
  std::cout << StrInterleaving("abd", "cef", "abcdef", m) << ":"
            << StrInterleaving("abd", "cef", "abcbef", m) << ":"
            << StrInterleaving("abc", "def", "abdccf", m) << ":"
            << StrInterleaving("abcdef", "mnop", "mnaobcdepf", m);
  return 0;
}

int StrInterleaving(std::string str1, std::string str2, std::string target,
                    Method m) {
  std::map<std::string, bool> dp;
  switch (m) {
    case Method::BRUTE:
      return Brute(str1, str2, target, 0, 0, 0);
    case Method::MEM:
      return Memoize(str1, str2, target, 0, 0, 0, dp);
    case Method::BU:
      return BU(str1, str2, target);
  }
}

int Brute(std::string str1, std::string str2, std::string target, int i1,
          int i2, int ti) {
  int len1 = str1.length();
  int len2 = str2.length();
  int len_t = target.length();
  if (i1 == len1 && i2 == len2 && ti == len_t) return true;
  if (ti == len_t) return false;
  bool b1 = false, b2 = false;
  if (i1 < len1 && str1[i1] == target[ti])
    b1 = Brute(str1, str2, target, i1 + 1, i2, ti + 1);
  if (i2 < len2 && str2[i2] == target[ti])
    b2 = Brute(str1, str2, target, i1, i2 + 1, ti + 1);
  return b1 || b2;
}

int Memoize(std::string str1, std::string str2, std::string target, int i1,
            int i2, int ti, std::map<std::string, bool>& dp) {
  int len1 = str1.length();
  int len2 = str2.length();
  int len_t = target.length();
  if (i1 == len1 && i2 == len2 && ti == len_t) return true;
  if (ti == len_t) return false;
  std::string k =
      std::to_string(i1) + "-" + std::to_string(i2) + "-" + std::to_string(ti);
  if (dp.find(k) == dp.end()) {
    bool b1 = false, b2 = false;
    if (i1 < len1 && str1[i1] == target[ti])
      b1 = Memoize(str1, str2, target, i1 + 1, i2, ti + 1, dp);
    if (i2 < len2 && str2[i2] == target[ti])
      b2 = Memoize(str1, str2, target, i1, i2 + 1, ti + 1, dp);
    dp.insert({k, b1 || b2});
  }
  return dp[k];
}

int BU(std::string str1, std::string str2, std::string target) {
  int len1 = str1.length();
  int len2 = str2.length();
  if (len1 + len2 != (int)target.length()) return false;

  std::vector<std::vector<bool>> dp(len1 + 1,
                                    std::vector<bool>(len2 + 1, false));
  dp[0][0] = true;
  for (int i = 1; i <= len1; ++i) dp[i][0] = target[i - 1] == str1[i - 1];

  for (int j = 1; j <= len2; ++j) dp[0][j] = target[j - 1] == str2[j - 1];

  for (int i = 1; i <= len1; ++i) {
    for (int j = 1; j <= len2; ++j) {
      int ti = i + j - 1;
      if (str1[i - 1] == target[ti])
        dp[i][j] = dp[i - 1][j];
      else if (str2[j - 1] == target[ti])
        dp[i][j] = dp[i][j] || dp[i][j - 1];
    }
  }
  return dp[len1][len2];
}
