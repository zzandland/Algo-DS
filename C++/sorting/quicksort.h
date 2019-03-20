#ifndef QUICKSORT_H
#define QUICKSORT_H

#include <algorithm>
#include <vector>

template <class T>
class Quicksort
{
public:
  static void Sort(std::vector<T>& arr);
private:
  static void Recursive(std::vector<T>& arr, int low, int high);

  static int Partition(std::vector<T>& arr, int low, int high);
};

template <class T>
void Quicksort<T>::Sort(std::vector<T>& arr)  {
  Recursive(arr, 0, arr.size() - 1);
}

template <class T>
void Quicksort<T>::Recursive(std::vector<T>& arr, int low, int high) {
  if (low < high) {
    int pi = Partition(arr, low, high);

    Recursive(arr, low, pi - 1);
    Recursive(arr, pi + 1, high);
  }
}

template <class T>
int Quicksort<T>::Partition(std::vector<T>& arr, int low, int high) {
  int pivot = arr[high];
  int i = low - 1;

  for (int j = low; j < high; ++j) {
    if (arr[j] < pivot) {
      std::swap(arr[++i], arr[j]);
    }
  }
  std::swap(arr[++i], arr[high]);
  return i;
}

#endif /* QUICKSORT_H */
