bool isAnagram(char* s, char* t) {
  int dic[26] = {0};
  for (int i = 0; i < strlen(s); i++) {
    dic[s[i] - 'a']++;
  }
  for (int j = 0; j < strlen(t); j++) {
    dic[t[j] - 'a']--;
  }
  for (int k = 0; k < 26; k++) {
    if (dic[k] != 0) return 0;
  }  
  return 1;
}