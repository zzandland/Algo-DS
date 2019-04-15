#include <iostream>

void NextNumber(int num);
int NextSmallerNumber(int num);
int NextLargerNumber(int num);
int ClearFrom0toP(int num);

int main(void) {
  NextNumber(10115);
  return 0;
}

void NextNumber(int num) {
  std::cout << "Next smaller number is: " << NextSmallerNumber(num)
            << std::endl;
  std::cout << "Next larger number is: " << NextLargerNumber(num) << std::endl;
}

int NextSmallerNumber(int num) {
  int cpy = num, c0 = 0, c1 = 0;

  while ((cpy & 1) == 1) {
    ++c1;
    cpy >>= 1;
  }

  if (cpy == 0)
    return -1;  // all bit in the number is 1; there cannot be a smaller value
                // with the same number of 1

  while ((cpy & 1) == 0 && cpy > 0) {
    ++c0;
    cpy >>= 1;
  }

  int i = c0 + c1;
  num &= (-1 << (i + 1));  // clear bits from 0 to i, inclusive
  int mask = (1 << (c1 + 1)) - 1; // sequence of 0 followed by c1 number of 1s
  mask <<= (c0 - 1); // followed by c0 - 1 number of 0s
  return num | mask;
}

int NextLargerNumber(int num) {
  int cpy = num, c1 = 0, c0 = 0;
  while ((cpy & 1) == 0 && cpy != 0) {
    ++c0;
    cpy >>= 1;
  }

  while ((cpy & 1) == 1) {
    ++c1;
    cpy >>= 1;
  }

  int i = c0 + c1;
  if (i == 31 || i == 0) return -1;
  num |= (1 << i);                 // flip bit 0 at ith pos to 1
  num &= ~((1 << i) - 1);          // clear bits from i to 0
  int mask = (1 << (c1 - 1)) - 1;  // add 1s to the rightmost
  return num | mask;
}
