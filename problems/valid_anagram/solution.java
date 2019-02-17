class Solution {
  public boolean isAnagram(String s, String t) {
    int dic[] = new int[26];
    for (int i = 0; i < s.length(); i++) {
      dic[s.charAt(i) - 'a']++;
    }
    for (int j = 0; j < t.length(); j++) {
      dic[t.charAt(j) - 'a']--;
    }
    for (int k = 0; k < dic.length; k++) {
      if (dic[k] != 0) return false;  
    }
    return true;
  }
}