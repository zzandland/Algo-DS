#ifndef SORTING_H
#define SORTING_H

#include <algorithm>
#include <iostream>
#include <vector>

template <class T> class Sorting {
public:
  void static Sort(char type, std::vector<T> &arr);

private:
  void static Heapsort(std::vector<T> &arr);

  void static Mergesort(std::vector<T> &arr, int begin, int end);

  void static Merge(std::vector<T> &arr, int begin, int end, int middle);

  void static Quicksort(std::vector<T> &arr, int begin, int end);

  void static Heapify(std::vector<T> &arr, int index, int delimiter);

  int static Partition(std::vector<T> &arr, int begin, int end);
};

template <class T> void Sorting<T>::Sort(char type, std::vector<T> &arr) {
  switch (type) {
  case 'H':
    Heapsort(arr);
    break;
  case 'Q':
    Quicksort(arr, 0, arr.size() - 1);
    break;
  case 'M':
    Mergesort(arr, 0, arr.size() - 1);
    break;
  }
};

template <class T> void Sorting<T>::Heapsort(std::vector<T> &arr) {
  for (int i = arr.size() / 2 - 1; i >= 0; --i) {
    Heapify(arr, i, arr.size());
  }

  for (int i = arr.size() - 1; i >= 0; --i) {
    std::swap(arr[0], arr[i]);
    Heapify(arr, 0, i);
  }
}

template <class T>
void Sorting<T>::Heapify(std::vector<T> &arr, int index, int delimiter) {
  int left = 2 * index + 1;
  int right = 2 * index + 2;
  int largest = index;

  if (left < delimiter && arr[largest] < arr[left])
    largest = left;

  if (right < delimiter && arr[largest] < arr[right])
    largest = right;

  if (largest != index) {
    std::swap(arr[index], arr[largest]);
    Heapify(arr, largest, delimiter);
  }
}

template <class T>
void Sorting<T>::Mergesort(std::vector<T> &arr, int begin, int end) {
  if (begin < end) {
    int middle = begin + (end - begin) / 2;
    Mergesort(arr, begin, middle);
    Mergesort(arr, middle + 1, end);
    Merge(arr, begin, end, middle);
  }
}

template <class T>
void Sorting<T>::Merge(std::vector<T> &arr, int begin, int end, int middle) {
  T temp[end - middle + 1];
  std::copy(arr.begin() + middle + 1, arr.begin() + end + 1, temp);

  int p1 = middle;
  int p2 = end - middle - 1;

  for (int i = end; p1 >= begin || p2 >= 0; --i) {
    if (p1 >= begin && p2 >= 0) {
      if (arr[p1] > temp[p2])
        arr[i] = arr[p1--];
      else
        arr[i] = temp[p2--];
    } else if (p1 >= begin) {
      arr[i] = arr[p1--];
    } else if (p2 >= 0) {
      arr[i] = temp[p2--];
    }
  }
}

template <class T>
void Sorting<T>::Quicksort(std::vector<T> &arr, int begin, int end) {
  if (begin < end) {
    int pi = Partition(arr, begin, end);
    Quicksort(arr, begin, pi - 1);
    Quicksort(arr, pi + 1, end);
  }
}

template <class T>
int Sorting<T>::Partition(std::vector<T> &arr, int begin, int end) {
  T pivot = arr[end];
  int i = begin - 1;
  for (int j = begin; j < end; ++j) {
    if (arr[j] < pivot)
      std::swap(arr[++i], arr[j]);
  }
  std::swap(arr[++i], arr[end]);

  return i;
}

#endif /* SORTING_H */
