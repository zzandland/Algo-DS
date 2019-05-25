class Solution {
public:
  bool isValid(string s) {
    stack<char> brackets;
    for (char c : s) {
      if (c == '(' || c == '{' || c == '[') {
        brackets.push(c);
      } else {
        if (brackets.empty()) return false;
        char open = brackets.top();
        brackets.pop();
        if (c == ')' && open != '(')
          return false;
        else if (c == '}' && open != '{')
          return false;
        else if (c == ']' && open != '[')
          return false;
      }
    }
    return brackets.empty();
  }
};