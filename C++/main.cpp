#include <iostream>
#include "sorting/quicksort.h"

int main(void)
{
  std::vector<int> arr = {158, 283, 128, 592, 234, 124};

  Quicksort::Sort(arr);

  for (size_t i = 0; i < arr.size(); ++i) {
    std::cout << arr[i] << " ";
  }
  return 0;
}
