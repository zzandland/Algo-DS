#ifndef MERGESORT_H
#define MERGESORT_H

#include <algorithm>
#include <vector>

#include <iostream>

template <class T>
class Mergesort {
 public:
  static void Sort(std::vector<int>& arr) { MergeSort(arr, 0, arr.size() - 1); }

 private:
  static void MergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
      int middle = left + (right - left) / 2;
      MergeSort(arr, left, middle);
      MergeSort(arr, middle + 1, right);
      Merge(arr, left, right, middle);
    }
  };

  static void Merge(std::vector<int>& arr, int left, int right, int middle) {
    int p1 = middle, p2 = right - middle - 1, p = right;
    int temp[right - middle];
    for (int i = middle + 1, j = 0; i <= right; ++i, ++j) temp[j] = arr[i];
    while (p1 >= 0 || p2 >= 0) {
      if (p1 >= 0 && p2 >= 0) {
        if (arr[p1] > temp[p2])
          arr[p--] = arr[p1--];
        else
          arr[p--] = temp[p2--];
      } else if (p1 >= 0) {
        arr[p--] = arr[p1--];
      } else if (p2 >= 0) {
        arr[p--] = temp[p2--];
      }
    }
  };
};

#endif /* MERGESORT_H */
