#include <iostream>

int PairwiseSwap(int num);

int main(void)
{
  std::cout << PairwiseSwap(17) << std::endl;
  return 0;
}

int PairwiseSwap(int num) {
  int swap = 0;
  while (num > 0) {
    int one = (num & 1);
    num >>= 1;
    int two = (num & 1);
    num >>= 1;
    swap <<= 1;
    swap += one;
    swap <<= 1;
    swap += two;
  }
  return swap;
}
