#include <iostream>
#include "printFunc.h"
#include "sorting/heapsort.h"
#include "sorting/quicksort.h"

int main(void)
{
  std::vector<int> arr = {158, 283, 128, 592, 234, 124};

  printArr<int>(arr, "Before sorting:");

  Heapsort<int>::Sort(arr);

  printArr<int>(arr, "After sorting:");

  return 0;
}

