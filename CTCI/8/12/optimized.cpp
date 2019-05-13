#include <iostream>
#include <vector>

class NQueens {
 public:
  NQueens(int n) : columns_(std::vector<int>(n, 0)), size_(n) {};

  void Print() {
    for (int row = 0; row < size_; ++row) {
      for (int col = 0; col < size_; ++col) {
        int out = (col == columns_[row]) ? 1 : 0;
        std::cout << out << " ";
      }
      std::cout << std::endl;
    }
  }

  int PlaceQueens (int row) {
    if (row == size_) {
      Print();
      std::cout << std::endl;
      return 1;
    } else {
      int out = 0;
      for (int col = 0; col < size_; ++col) {
        if (CheckValid(row, col)) {
          columns_[row] = col;
          out += PlaceQueens(row + 1);
        }
      }
      return out;
    }
  }

  bool CheckValid(int row1, int col1) {
    for (int row2 = 0; row2 < row1; ++row2) {
      int col2 = columns_[row2];
      if (col1 == col2) return false;
      int col_dist = std::abs(col1 - col2);
      int row_dist = row1 - row2;
      if (col_dist == row_dist) return false;
    }  
    return true;
  }

 private:
  std::vector<int> columns_;
  int size_;
};

int main(void)
{
  NQueens* n = new NQueens(11);
  std::cout << n->PlaceQueens(0);
  return 0;
}
