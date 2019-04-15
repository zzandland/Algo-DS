#include <iostream>

void NextNumber(int num);
int NextSmallerNumber(int num);
int NextLargerNumber(int num);

int main(void)
{
  NextNumber(55);
  return 0;
}

void NextNumber(int num) {
  if ((-1 & num) == -1) {
    std::cerr << "There's no smaller number." << std::endl;
    exit(1);
  }
  std::cout << "Next smaller number is: " << NextSmallerNumber(num) << std::endl;
  std::cout << "Next larger number is: " << NextLargerNumber(num) << std::endl;
}

int NextSmallerNumber(int num) {
  int cpy = num, prev = 1, i = 0;
  while (cpy != 0) {
    if ((cpy & 1) != 0 && prev == 0) break;
    else prev = cpy & 1;
    cpy >>= 1;
    ++i;
  }
  int mask = ~(1 << i);
  return (num & mask) | (1 << (i - 1));
}

int NextLargerNumber(int num) {
  int cpy = num, prev = 0, i = 0;
  bool found = false;
  while (cpy != 0) {
    if ((cpy & 1) == 0 && prev == 1) {
      found = true;
      break;
    } else {
      prev = cpy & 1;
    }
    cpy >>= 1;
    ++i;
  }
  if (!found) return num << 1;
  int mask = ~(1 << (i - 1));
  return (num & mask) | (1 << i);
}
