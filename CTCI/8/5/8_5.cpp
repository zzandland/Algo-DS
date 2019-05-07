#include <iostream>

int RecursiveMultiply(int n, int m);
int RecursiveDivide(int n, int m);

int main(void) {
  std::cout << RecursiveDivide(15, 2);
  return 0;
}

int RecursiveMultiply(int n, int m) {
  if (m == 0) return 0;
  if (m & 1)
    return n + RecursiveMultiply(n << 1, m >> 1);
  else
    return RecursiveMultiply(n << 1, m >> 1);
}

int RecursiveDivide(int n, int m) {
  if (m == 0) return 0;
  if (m & 1)
    return n + RecursiveDivide(n >> 1, m >> 1);
  else
    return RecursiveDivide(n >> 1, m >> 1);
}
