#include <iostream>

std::string BinaryToString(double num);

int main(void)
{
  std::cout << BinaryToString(0.3592);
  return 0;
}

std::string BinaryToString(double num) {
  if (num >= 1 || num <= 0) return "ERROR";
  std::string binary = ".";
  double val = 1;
  for (int i = 0; i < 32; ++i) {
    val /= 2;
    if (num == val) {
      binary += "1";
      return binary;
    } else if (num > val) {
      binary += "1";
      num -= val;
    } else {
      binary += "0";
    }
  }
  return binary;
}
