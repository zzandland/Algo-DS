#include "quicksort.h"

void Quicksort::Sort(std::vector<int>& arr) {
  Recursive(arr, 0, arr.size() - 1);
}

void Quicksort::Recursive(std::vector<int>& arr, int low, int high) {
  if (low < high) {
    int pi = Partition(arr, low, high);

    Recursive(arr, low, pi - 1);
    Recursive(arr, pi + 1, high);
  }
}

int Quicksort::Partition(std::vector<int>& arr, int low, int high) {
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
