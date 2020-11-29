// DFS of Undirected Graph

#include <stdio.h>
#include <stdlib.h>

int** create_adj_mt(int V) {
  int **mt = (int**)malloc(sizeof(int) * V * V);
  for (int i = 0; i < V; ++i) {
    mt[i] = (int*)malloc(sizeof(int) * V);
    for (int j = 0; j < V; ++j) mt[i][j] = 0;
  }
  return mt;
}

void dfs(int n, int V, int **adj_mt, int *visited) {
  printf("%d ", n);
  visited[n] = 1;
  for (int i = 0; i < V; ++i) {
    if (adj_mt[n][i] && !visited[i]) {
      dfs(i, V, adj_mt, visited);
    }
  }
}

int main() {
  int V, E, S;
  scanf(" %d %d %d", &V, &E, &S);
  int** adj_mt = create_adj_mt(V);
  int visited[V];
  for (int i = 0; i < V; ++i) visited[i] = 0;

  int u, v;
  for (int i = 0; i < E; ++i) {
    scanf(" %d %d", &u, &v);
    adj_mt[u][v] = 1;
    adj_mt[v][u] = 1;
  }

  dfs(S, V, adj_mt, visited);

  return 0;
}
