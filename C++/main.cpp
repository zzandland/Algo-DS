#include <chrono>
#include <iostream>
#include <random>
#include "print.h"
#include "sorting.h"

void MeasureSortingTime(char type, void (*sortFun)(char type, std::vector<int>& arr), std::vector<int> arr);

int main(void) {
  std::default_random_engine generator;
  std::uniform_int_distribution<int> ran_num(1, 3000);

  std::vector<int> arr;

  for (int i = 0; i < 1000000; ++i)
    arr.push_back(ran_num(generator));

  void (*sorting)(char type, std::vector<int>& arr);

  sorting = Sorting<int>::Sort;

  std::cout << "\nHeapsort\n";
  MeasureSortingTime('H', sorting, arr);

  std::cout << "\nQuicksort\n";
  MeasureSortingTime('Q', sorting, arr);

  std::cout << "\nMergesort\n";
  MeasureSortingTime('M', sorting, arr);

  return 0;
}

void MeasureSortingTime(char type, void (*sortFun)(char type, std::vector<int>& arr), std::vector<int> arr) {
  auto start = std::chrono::system_clock::now();

  // printArr<int>(arr, "Before sorting:");

  sortFun(type, arr);

  // printArr<int>(arr, "After sorting:");

  auto end = std::chrono::system_clock::now();

  std::chrono::duration<double> diff = end - start;

  std::cout << "The time took to run the function: " << diff.count() << " s\n";
}
