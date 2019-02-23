import java.util.HashSet;

class Solution {
  public int numJewelsInStones(String J, String S) {
    HashSet<Character> jewelSet = new HashSet<Character>();
    for (int i = 0; i < J.length(); i++) {
      jewelSet.add(J.charAt(i));  
    }
    
    int nType = 0;
    
    for (int j = 0; j < S.length(); j++) {
      if (jewelSet.contains(S.charAt(j))) nType++;
    }
    
    return nType;
  }
}