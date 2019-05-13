#include <iostream>
#include <vector>

class Board {
public:
  Board(int n) : board_(std::vector<std::vector<bool>>(n, std::vector<bool>(n, false))), len_(n) {};

  void Print() {
    for (int i = 0; i < len_; ++i) {
      for (int j = 0; j < len_; ++j)
        std::cout << board_[i][j] << " ";
      std::cout << std::endl;
    }
  }

  bool CheckConflict(std::pair<int, int>& pos) {
    return CheckHor(pos) || CheckVer(pos) || CheckDiag(pos);
  }

  bool CheckHor(std::pair<int, int>& pos) {
    for (int i = 0; i < len_; ++i)
      if (i != pos.second && board_[pos.first][i]) return true;
    return false;
  }

  bool CheckVer(std::pair<int, int>& pos) {
    for (int i = 0; i < len_; ++i)
      if (i != pos.first && board_[i][pos.second]) return true;
    return false;
  }

  bool CheckDiag(std::pair<int, int>& pos) {
    int row = pos.first;
    int col = pos.second;
    for (int i = 1; i < len_; ++i) {
      if (row + i < len_ && col + i < len_) {
        if (board_[row + i][col + i]) return true;
      }

      if (row + i < len_ && col - i >= 0) {
        if (board_[row + i][col - i]) return true;
      }

      if (row - i >= 0 && col + i < len_) {
        if (board_[row - i][col + i]) return true;
      }

      if (row - i >= 0 && col - i >= 0) {
        if (board_[row - i][col - i]) return true;
      }
    }  
    return false;
  }

  void EightQueens() {
    std::pair<int, int> init(0, 0);
    std::cout << EightQueens(init, 0);
  };

  int EightQueens(std::pair<int, int>& pos, int count) {
    int row = pos.first;
    int col = pos.second;
    std::pair<int, int> nxt_row(row + 1, 0);
    std::pair<int, int> nxt_col(row, col + 1);

    if (row == len_) return 0;

    if (count == len_) {
      Print();
      std::cout << std::endl;
      return 1;
    }

    if (row < len_ && col >= len_) {
      return EightQueens(nxt_row, count);
    }

    int output = 0;

    if (!CheckConflict(pos)) {
      board_[row][col] = true;
      output += EightQueens(nxt_col, count + 1);
      board_[row][col] = false;
    }
    return output + EightQueens(nxt_col, count);
  }

  std::vector<std::vector<bool>> board_;
  int len_;
};


int main(void)
{
  Board* b = new Board(10);
  b->EightQueens();
  delete b;
  return 0;
}
