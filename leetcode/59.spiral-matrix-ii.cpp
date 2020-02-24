/*
 * @lc app=leetcode id=59 lang=cpp
 *
 * [59] Spiral Matrix II
 *
 * https://leetcode.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (51.14%)
 * Likes:    768
 * Dislikes: 100
 * Total Accepted:    172.5K
 * Total Submissions: 337.2K
 * Testcase Example:  '3'
 *
 * Given a positive integer n, generate a square matrix filled with elements
 * from 1 to n^2 in spiral order.
 * 
 * Example:
 * 
 * 
 * Input: 3
 * Output:
 * [
 * ⁠[ 1, 2, 3 ],
 * ⁠[ 8, 9, 4 ],
 * ⁠[ 7, 6, 5 ]
 * ]
 * 
 * 
 */
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
  void right(vector<vector<int>> &matrix, int y, int x, int num) {
    matrix[y][x] = ++num;
    while (x < matrix[0].size() - 1 && !matrix[y][x + 1]) {
      matrix[y][++x] = ++num;
      if (x == matrix[0].size() - 1) {
        break;
      }
    }
    if (matrix[y + 1][x] == 0) {
      ++y;
      down(matrix, y, x, num);
    }
  }

  void down(vector<vector<int>> &matrix,  int y, int x, int num) {
    matrix[y][x] = ++num;
    while (y < matrix[0].size() - 1 && !matrix[y + 1][x]) {
      matrix[++y][x] = ++num;
      if (y == matrix[0].size() - 1) {
        break;
      }
    }
    if (matrix[y][x - 1] == 0) {
      --x;
      left(matrix, y, x, num);
    }
  }

  void left(vector<vector<int>> &matrix,  int y, int x, int num) {
    matrix[y][x] = ++num;
    while (x > 0 && !matrix[y][x - 1]) {
      matrix[y][--x] = ++num;
      if (x == 0) {
        break;
      }
    }
    if (matrix[y - 1][x] == 0) {
      --y;
      up(matrix, y, x, num);
    }
  }

  void up(vector<vector<int>> &matrix,  int y, int x, int num) {
    matrix[y][x] = ++num;
    while (y > 0 && !matrix[y - 1][x]) {
      matrix[--y][x] = ++num;
      if (y == 0) {
        break;
      }
    }
    if (matrix[y][x + 1] == 0) {
      ++x;
      right(matrix, y, x, num);
    }
  }

  vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    int num = 0;
    if (n == 1) {
      matrix[0][0] = 1;
    } else if (n > 1) {
      right(matrix, 0, 0, num);
    }
    return matrix;
  }
};
// @lc code=end
