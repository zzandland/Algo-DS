#include <iostream>

int Insertion(int N, int M, int i, int j);
bool GetBit(int num, int i);
int UpdateBit(int num, int i, bool bit_is_1);

int main(void)
{
  std::cout << Insertion(1024, 19, 2, 6);
  return 0;
}

int Insertion(int N, int M, int i, int j) {
  int left = ~0 << (j + 1);
  int right = (1 << i) - 1;
  int mask = left | right;
  return (N & mask) | (M << i);
}
