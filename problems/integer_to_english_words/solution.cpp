class Solution {
public:
  string numberToWords(int num) {
    if (num == 0) return "Zero";
    list<int> num_arr = divideByThousand(num);
    string thousands[4] = {"", "Thousand", "Million", "Billion"};
    string output = "";
    int counter = num_arr.size() - 1;
    for (auto it = num_arr.begin(); it != num_arr.end(); ++it) {
      int hundred = *it;
      if (hundred > 0) {
        if (it != num_arr.begin()) output += " ";
        output += hundredToString(hundred);
        if (counter > 0) output += " " + thousands[counter];
      }
      --counter;
    }
    return output;
  }
  
  list<int> divideByThousand(int num) {
    list<int> num_arr;
    while (num > 0) {
      num_arr.push_front(num % 1000);
      num /= 1000;
    }
    return num_arr;
  }
  
  string hundredToString(int num) {
    string singles[10] = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    string decimals[10] = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    string tenth[10] = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    string output = "";
    if (num >= 100) {
      output += singles[num / 100] + " Hundred";
      num %= 100;
      if (num > 0) output += " ";
    }
    if (num >= 20) {
      output += decimals[num / 10];
      num %= 10;
      if (num > 0) output += " ";
    } else if (num >= 10) {
      output += tenth[num % 10];
      return output;
    } 
    if (num > 0)
      output += singles[num];
    return output;
  }
};