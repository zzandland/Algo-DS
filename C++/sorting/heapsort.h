#ifndef HEAPSORT_H
#define HEAPSORT_H

#include <vector>

class Heapsort {
 public:
  static void Sort(std::vector<int>& arr);

 private:
  static void Heapify(std::vector<int>& arr, int index, int delimiter);

  static void BuildHeap(std::vector<int>& arr);
};

#endif /* HEAPSORT_H */
