#include <iostream>
#include <vector>
#include <cmath>

int FlipBitToWin(int num);

int main(void)
{
  std::cout << FlipBitToWin(1024);
  return 0;
}

int FlipBitToWin(int num) {
  int curr_counter = 0;
  int prev_counter = 0;
  int max_counter = 1; // the minimum length is always 1
  while (num != 0) {
    if ((num & 1) == 0) {
      int sum = curr_counter + prev_counter;
      if (sum > max_counter) max_counter = sum;
      prev_counter = curr_counter;
      curr_counter = 0;
    } else {
      curr_counter++;
    }
    num >>= 1;
  }
  return max_counter + 1;
}
