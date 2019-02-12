class Solution {
  public int firstUniqChar(String s) {
    int[] dic = new int[26];
    int[] index = new int[26];
    
    for (int i = 0; i < s.length(); i++) {
      int cha = s.charAt(i) - 'a';
      if (dic[cha] == 0) index[cha] = i;
      dic[cha]++;
    }
    
    for (int j = 0; j < s.length(); j++) {
      int cha = s.charAt(j) - 'a';
      if (dic[cha] == 1) return index[cha];
    }
    return -1;
  }
}