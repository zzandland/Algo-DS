#ifndef HEAPSORT_H
#define HEAPSORT_H

#include <vector>

class HeapSort {
 public:
  static void Sort(std::vector<int>& arr);

 private:
  static void Heapify(std::vector<int>& arr, int index, int delimiter);

  static void BuildHeap(std::vector<int>& arr);
};

#endif /* HEAPSORT_H */
