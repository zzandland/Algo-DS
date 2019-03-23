#ifndef PRINTFUNC_H
  #define PRINTFUNC_H

#include <iostream>
#include <vector>

template <class T>
void printArr(std::vector<T> arr, std::string msg) {
  std::cout << msg << std::endl;
  for (size_t i = 0; i < arr.size(); i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;
}

#endif /* PRINTFUNC_H */
