#include <iostream>
#include <vector>

void Parens(int n);
void Parens(int open, int close, std::string parens);

int main(void)
{
  Parens(10);  
  return 0;
}

void Parens(int n) {
  Parens(n, n, "");
}

void Parens(int open, int close, std::string parens) {
  if (close < open || close < 0 || open < 0) return;
  if (open == 0 && close == 0) {
    std::cout << parens << std::endl;
    return;
  }
  Parens(open - 1, close, parens + '(');
  Parens(open, close - 1, parens + ')');
}
