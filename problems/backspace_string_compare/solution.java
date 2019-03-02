class Solution {
  public boolean backspaceCompare(String S, String T) {
    int i = S.length() - 1;
    int j = T.length() - 1;
    int iCnt = 0; 
    int jCnt = 0;
    
    while (i >= 0 || j >= 0) {
      while (i >= 0) {
        if (S.charAt(i) == '#') { iCnt++;  i--; }
        else if (iCnt > 0) { iCnt--; i--; }
        else break;
      } 
      
      while (j >= 0) {
        if (T.charAt(j) == '#') { jCnt++; j--; }
        else if (jCnt > 0) { jCnt--; j--; }
        else break;
      }
      
      if (i >= 0 && j >= 0 && S.charAt(i) != T.charAt(j)) return false;
      if ((i >= 0) != (j >= 0)) return false;
      
      i--; j--;
    }
    
    return true;
  }
}