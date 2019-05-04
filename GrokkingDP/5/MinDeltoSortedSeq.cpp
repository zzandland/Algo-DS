#include <iostream>
#include <vector>

enum class Method {
  BRUTE, MEM, BU
};

int MinDeltoSortedSeq(std::vector<int>& nums, Method m);
int Brute(std::vector<int>& nums);

int main(void)
{
  
  return 0;
}

int MinDeltoSortedSeq(std::vector<int>& nums, Method m) {
  switch (m) {
    case Method::BRUTE:
      return Brute(nums, 1)
  }
}
