class Solution {
  public String numberToWords(int num) {
    if (num == 0) return "Zero";
    StringBuilder output = new StringBuilder();
    int threeDigit = 0;
    while (num > 0) {
      if (num % 1000 != 0) output.insert(0, convertToWord(num % 1000, threeDigit));
      num /= 1000;
      threeDigit++;
    }
    return output.toString().trim();
  }
  
  private String convertToWord(int number, int threeDigit) {
    StringBuilder wordBuild = new StringBuilder();
    if (number >= 100) {
      wordBuild.append(String.format(" %s Hundred", getDigitName(number / 100)));
      number %= 100;
    }
    if (number >= 20) {
      wordBuild.append(String.format(" %s", getTenthName(number / 10)));
      number %= 10;
    }
    if (number >= 10) {
      wordBuild.append(String.format(" %s", getOneTenthName(number)));
    } else if (number > 0) {
      wordBuild.append(String.format(" %s", getDigitName(number)));
    }
    if (wordBuild.length() > 0) wordBuild.append(String.format(" %s", getThreeDigitName(threeDigit)));
    return wordBuild.toString();
  }
  
  private String getThreeDigitName(int order) {
    switch (order) {
      case 1: return "Thousand";
      case 2: return "Million";
      case 3: return "Billion";
    }
    return "";
  }
  
  private String getDigitName(int number) {
    switch (number) {
      case 1: return "One";
      case 2: return "Two";
      case 3: return "Three";
      case 4: return "Four";
      case 5: return "Five";
      case 6: return "Six";
      case 7: return "Seven";
      case 8: return "Eight";
      case 9: return "Nine";
    }  
    return "";
  }
  
  private String getTenthName(int number) {
    switch (number) {
      case 2: return "Twenty";
      case 3: return "Thirty";
      case 4: return "Forty";
      case 5: return "Fifty";
      case 6: return "Sixty";
      case 7: return "Seventy";
      case 8: return "Eighty";
      case 9: return "Ninety";
    }  
    return "";
  }
  
  private String getOneTenthName(int number) {
    switch (number) {
      case 10: return "Ten";
      case 11: return "Eleven";
      case 12: return "Twelve";
      case 13: return "Thirteen";
      case 14: return "Fourteen";
      case 15: return "Fifteen";
      case 16: return "Sixteen";
      case 17: return "Seventeen";
      case 18: return "Eighteen";
      case 19: return "Nineteen";
    }
    return "";
  }
}