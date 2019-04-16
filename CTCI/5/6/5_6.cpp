#include <iostream>

int Conversion(int n1, int n2);

int main(void) {
  int n1 = 1100;
  int n2 = 19;
  std::cout << "Number of digits need to be switched from " << n1 << " to get "
            << n2 << " is " << Conversion(n1, n2) << "." << std::endl;
  return 0;
}

int Conversion(int n1, int n2) {
  int cnt = 0;
  for (int c = n1 ^ n2; c > 0; c = c & (c - 1))
    ++cnt;
  return cnt;
}
