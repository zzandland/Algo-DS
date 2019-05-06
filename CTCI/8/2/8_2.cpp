#include <iostream>
#include <list>
#include <time.h>
#include <vector>

struct Point {
  int y;
  int x;
};

std::list<Point*> FindPath(std::vector<std::vector<bool>>& grid);
bool FindPath(std::vector<std::vector<bool>>& grid, size_t i, size_t j,
              std::list<Point*>& path, std::vector<std::vector<bool>>& dp);

int main(void) {
  std::srand(time(0));
  std::vector<std::vector<bool>> grid(5, std::vector<bool>(4));
  for (size_t i = 0; i < grid.size(); ++i) {
    for (size_t j = 0; j < grid[i].size(); ++j) {
      grid[i][j] = (std::rand() % 10 > 1) ? true : false;
      if (!grid[i][j]) std::cout << "false: " << i << " " << j << std::endl;
    }
  }
  std::list<Point*> path = FindPath(grid);
  for (Point* c : path) std::cout << c->y << ":" << c->x << std::endl;
  return 0;
}

std::list<Point*> FindPath(std::vector<std::vector<bool>>& grid) {
  std::list<Point*> path;
  std::vector<std::vector<bool>> dp(grid.size(),
                                    std::vector<bool>(grid[0].size()));
  if (FindPath(grid, 0, 0, path, dp)) return path;
  return path;
}

bool FindPath(std::vector<std::vector<bool>>& grid, size_t i, size_t j,
              std::list<Point*>& path, std::vector<std::vector<bool>>& dp) {
  if (i == grid.size() || j == grid[0].size() || !grid[i][j]) return false;
  if (i == grid.size() - 1 && j == grid[0].size() - 1) return true;
  if (!dp[i][j]) {
    dp[i][j] = true;
    if (FindPath(grid, i + 1, j, path, dp) ||
        FindPath(grid, i, j + 1, path, dp)) {
      Point* p = new Point;
      p->y = i;
      p->x = j;
      path.push_front(p);
      return true;
    }
  }
  return false;
}
