#include <algorithm>
#include "heapsort.h"

#include <iostream>

void Heapsort::Sort(std::vector<int>& arr) {
  BuildHeap(arr);

  for (int i = arr.size() - 1; i >= 0; --i) {
    std::swap(arr[0], arr[i]);
    Heapify(arr, 0, i);
  }
}

void Heapsort::Heapify(std::vector<int>& arr, int index, int delimiter) {
  int left = 2 * index + 1;
  int right = 2 * index + 2;
  int largest = index;

  if (left < delimiter && arr[left] > arr[largest])
    largest = left;

  if (right < delimiter && arr[right] > arr[largest])
    largest = right;

  if (largest != index) {
    std::swap(arr[index], arr[largest]);
    Heapify(arr, largest, delimiter);
  }
}

void Heapsort::BuildHeap(std::vector<int>& arr) {
  int len = arr.size();
  for (int i = len / 2 - 1; i >= 0; --i) {
    Heapify(arr, i, len);
  }
}
