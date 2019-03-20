#ifndef HEAPSORT_H
#define HEAPSORT_H

#include <algorithm>
#include <iostream>
#include <vector>

template <class T>
class Heapsort {
 public:
  static void Sort(std::vector<T>& arr);

 private:
  static void Heapify(std::vector<T>& arr, int index, int delimiter);

  static void BuildHeap(std::vector<T>& arr);
};

template <class T>
void Heapsort<T>::Sort(std::vector<T>& arr) {
  BuildHeap(arr);

  for (int i = arr.size() - 1; i >= 0; --i) {
    std::swap(arr[0], arr[i]);
    Heapify(arr, 0, i);
  }
}

template <class T>
void Heapsort<T>::Heapify(std::vector<T>& arr, int index, int delimiter) {
  int left = 2 * index + 1;
  int right = 2 * index + 2;
  int largest = index;

  if (left < delimiter && arr[left] > arr[largest]) largest = left;

  if (right < delimiter && arr[right] > arr[largest]) largest = right;

  if (largest != index) {
    std::swap(arr[index], arr[largest]);
    Heapify(arr, largest, delimiter);
  }
}

template <class T>
void Heapsort<T>::BuildHeap(std::vector<T>& arr) {
  int len = arr.size();
  for (int i = len / 2 - 1; i >= 0; --i) {
    Heapify(arr, i, len);
  }
}

#endif /* HEAPSORT_H */
