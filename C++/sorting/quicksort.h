#ifndef QUICKSORT_H
#define QUICKSORT_H

#include <algorithm>
#include <vector>

class Quicksort
{
public:
  static void Sort(std::vector<int>& arr);
private:
  static void Recursive(std::vector<int>& arr, int low, int high);

  static int Partition(std::vector<int>& arr, int low, int high);
};

#endif /* QUICKSORT_H */
