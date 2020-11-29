// 섬의 개수

#include <stdio.h>
#include <stdlib.h>

typedef int coord[2];

coord dir[] = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};

void dfs(int **grid, int y, int x, int h, int w) {
  for (int i = 0; i < 9; ++i) {
    int ny = y + dir[i][0], nx = x + dir[i][1];
    if (0 <= ny && ny < h && 0 <= nx && nx < w && grid[ny][nx] == 1) {
      grid[ny][nx] = 0;
      dfs(grid, ny, nx, h, w);
    }
  }
}

int** create_matrix(int h, int w) {
  int **mt = (int**)malloc(sizeof(int) * h * w);
  for (int i = 0; i < h; ++i) mt[i] = (int*)malloc(sizeof(int) * w);
  return mt;
}

void delete_matrix(int **mt, int h) {
  for (int i = 0; i < h; ++i) free(mt[i]);
  free(mt);
}

int main() {
  int w, h, t;
  scanf(" %d %d", &w, &h);

  int **grid = create_matrix(h, w);

  for (int y = 0; y < h; ++y) {
    for (int x = 0; x < w; ++x) {
      scanf(" %d", &t);
      grid[y][x] = t;
    }
  }

  int res = 0;

  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      if (grid[i][j] == 1) {
        res++;
        grid[i][j] = 0;
        dfs(grid, i, j, h, w);
      }
    }
  }

  printf("%d", res);

  delete_matrix(grid, h);
  
  return 0;
}
