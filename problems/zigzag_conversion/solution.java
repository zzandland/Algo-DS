import java.util.ArrayList;

class Solution {
    public char[] splitStrToCharArr(String s) {
      char[] output = new char[s.length()];
      for (int i = 0; i < s.length(); i++) {
        output[i] = s.charAt(i);
      }
      return output;
    }
  
    public void addZigZag(ArrayList<ArrayList<Character>>zigzag, char[] charArr, int numRows) {
      int charIndex = 0;
      int arrIndex = 0;
      int charArrLen = charArr.length;
      while (charIndex < charArrLen) {
        while (arrIndex < numRows - 1 && charIndex < charArrLen) {
          if (charIndex == charArrLen) break;
          zigzag.get(arrIndex).add(charArr[charIndex]);
          arrIndex++;
          charIndex++;
        }
        while (arrIndex > 0 && charIndex < charArrLen) {
          if (charIndex == charArrLen) break;
          zigzag.get(arrIndex).add(charArr[charIndex]);
          arrIndex--;
          charIndex++;
        }
      }
    }
  
    public void addBreathFirst(ArrayList<ArrayList<Character>> zigzag, StringBuilder strBuilder) {
      for (int j = 0; j < zigzag.size(); j++) {
        for (int k = 0; k < zigzag.get(j).size(); k++) {
          strBuilder.append(zigzag.get(j).get(k));
        }
      }
    }

    public String convert(String s, int numRows) {
      if (numRows == 1) return s;
      char[] charArr = this.splitStrToCharArr(s);
      StringBuilder output = new StringBuilder();
      ArrayList<ArrayList<Character>> zigzag = new ArrayList<ArrayList<Character>>();
      for (int i = 0; i < numRows; i++) {
        ArrayList<Character> arr = new ArrayList<Character>();
        zigzag.add(i, arr);
      }
      this.addZigZag(zigzag, charArr, numRows);
      this.addBreathFirst(zigzag, output);
      return output.toString();
    }
}