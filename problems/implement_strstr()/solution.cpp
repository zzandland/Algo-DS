class Solution {
public:
  int strStr(string haystack, string needle) {
    if (needle.length() == 0) return 0;
    for (size_t i = 0; i < haystack.length(); ++i) {
      size_t j = 0;
      if (haystack[i] == needle[j]) {
        for (; j < needle.length(); ++j) {
          if (i + j == haystack.length() || haystack[i + j] != needle[j])
            break;
        }
        if (j == needle.length()) return i;
      }
    }
    return -1;
  }
};