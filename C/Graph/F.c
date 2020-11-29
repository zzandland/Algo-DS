#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *arr;
  int size;
} Stack;

Stack* create_st(int cap) {
  Stack *st = (Stack*)malloc(sizeof(Stack)); 
  st->arr = (int*)malloc(sizeof(int) * cap);
  st->size = -1;
  return st;
}

void delete_st(Stack *st) {
  free(st->arr);
  free(st);
}

void enqueue(Stack *st, int val) {
  st->arr[++st->size] = val;
}

int dequeue(Stack *st) {
  return st->arr[st->size--];
}

int** create_adj_mt(int V) {
  int **mt = (int**)malloc(sizeof(int) * V * V);
  for (int i = 0; i < V; ++i) {
    mt[i] = (int*)malloc(sizeof(int) * V);
    for (int j = 0; j < V; ++j) mt[i][j] = 0;
  }
  return mt;
}

void delete_adj_mt(int **mt, int V) {
  for (int i = 0; i < V; ++i) free(mt[i]);
  free(mt);
}

void dfs(int n, int V, int **adj_mt, int *visited, Stack *st) {
  if (visited[n]) return;
  visited[n] = 1;

  for (int i = 0; i < V; ++i) {
    if (adj_mt[n][i]) dfs(i, V, adj_mt, visited, st);
  }

  enqueue(st, n);
}

int main() {
  int T, V, E;
  scanf(" %d", &T);

  for (int i = 0; i < T; ++i) {
    scanf(" %d %d", &V, &E);

    int** adj_mt = create_adj_mt(V);
    int visited[V];
    for (int i = 0; i < V; ++i) visited[i] = 0;

    int u, v;
    for (int i = 0; i < E; ++i) {
      scanf(" %d %d", &u, &v);
      adj_mt[u][v] = 1;
    }

    Stack *st = create_st(V);

    for (int i = 0; i < V; ++i) dfs(i, V, adj_mt, visited, st);

    for (int i = 0 ; i < V; ++i) printf("%d ", dequeue(st));
    printf("\n");

    delete_adj_mt(adj_mt, V);
    delete_st(st);
  }

  return 0;
}
