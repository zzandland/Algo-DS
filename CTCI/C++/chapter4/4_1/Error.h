#ifndef ERROR_H
#define ERROR_H

#include <iostream>

class Error {
 public:
  Error(std::string msg);

  void print();

 private:
  std::string msg_;
};

Error::Error(std::string msg) { msg_ = msg; }

void Error::print() { std::cout << msg_ << std::endl; }

#endif /* ERROR_H */
