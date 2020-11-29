#include <stdio.h>
#include <stdlib.h>

int* create_edge(int u, int v, int w) {
  int* edge = (int*)malloc(sizeof(int) * 3);
  edge[0] = u;
  edge[1] = v;
  edge[2] = w;
  return edge;
}

int** create_edges(int E) {
  int** edges = (int**)malloc(sizeof(int) * E * 3);
  for (int i = 0; i < E; ++i) edges[i] = (int*)malloc(sizeof(int) * 3);
  return edges;
}

void delete_edges(int **edges, int E) {
  for (int i = 0; i < E; ++i) free(edges[i]);
  free(edges);
}

int comp(const void *a, const void *b) {
  int aw = ((int*) a)[2];
  int bw = ((int*) b)[2];
  return aw < bw ? -1 : aw == bw ? 0 : 1;
}

int main() {
  int V, E, u, v, w;
  scanf(" %d %d", &V, &E);

  int** edges = create_edges(E);
  for (int i = 0; i < E; ++i) {
    scanf(" %d %d %d", &u, &v, &w);
    edges[i] = create_edge(u, v, w);
  }

  qsort(edges, E, *edges, comp);

  for (int i = 0; i < E; ++i) {
    for (int j = 0; j < 3; ++j) printf("%d ", edges[i][j]);
    printf("\n");
  }

  return 0;
}
