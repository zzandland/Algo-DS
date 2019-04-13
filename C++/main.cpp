#include <chrono>
#include <iostream>
#include <random>
#include "bit_func.h"
#include "print.h"
#include "sorting.h"

void MeasureSortingTime(char type,
                        void (*sortFun)(char type, std::vector<int>& arr),
                        std::vector<int> arr);

int main(void) {
  std::cout << "Bit at 0th position of 22 is: " << GetBit(22, 0) << std::endl;
  std::cout << "Bit at 4th position of 22 is: " << GetBit(22, 4) << std::endl;
  std::cout << "Setting bit at 0th pos of 22 is 23: " << SetBit(22, 0)
            << std::endl;
  std::cout << "Setting bit at 1th pos of 22 is 22: " << SetBit(22, 1)
            << std::endl;
  std::cout << "Setting bit at 3th pos of 22 is 30: " << SetBit(22, 3)
            << std::endl;
  std::cout << "Clearing bit at 0th pos of 22 is 22: " << ClearBit(22, 0)
            << std::endl;
  std::cout << "Clearing bit at 1th pos of 22 is 20: " << ClearBit(22, 1)
            << std::endl;
  std::cout << "Clearing bits from MS to 2th pos of 22 is 2: "
            << ClearBitsMSBthrouthI(22, 2) << std::endl;
  std::cout << "Clearing bits from MS to 4th pos of 22 is 6: "
            << ClearBitsMSBthrouthI(22, 4) << std::endl;
  std::cout << "Clearing bits from 3rd to end of 22 is 16: "
            << ClearBitsIthrough0(22, 3) << std::endl;
  std::cout << "Update 2nd bit of 22 with 0 is 18: "
            << UpdateBit(22, 2, false) << std::endl;
  // std::default_random_engine generator;
  // std::uniform_int_distribution<int> ran_num(1, 3000);
  return 0;
}

void MeasureSortingTime(char type,
                        void (*sortFun)(char type, std::vector<int>& arr),
                        std::vector<int> arr) {
  auto start = std::chrono::system_clock::now();

  // printArr<int>(arr, "Before sorting:");

  sortFun(type, arr);

  // printArr<int>(arr, "After sorting:");

  auto end = std::chrono::system_clock::now();

  std::chrono::duration<double> diff = end - start;

  std::cout << "The time took to run the function: " << diff.count() << " s\n";
}
