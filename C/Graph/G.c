#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int val;
  struct Node *next;
} Node;

Node* create_node(int val) {
  Node* node = (Node*)malloc(sizeof(Node));
  node->val = val;
  node->next = NULL;
  return node;
}

typedef struct {
  Node *head, *tail;
  int len;
} Queue;

Queue* create_queue() {
  Queue* q = (Queue*)malloc(sizeof(Queue));
  q->head = q->tail = NULL;
  q->len = 0;
  return q;
}

void delete_queue(Queue *q) {
  while (q->head) {
    Node* tmp = q->head;
    q->head = q->head->next;
    free(tmp);
  }
}

void enqueue(Queue *q, int val) {
  q->len++;
  Node *tmp = create_node(val);
  if (q->tail) q->tail->next = tmp;
  q->tail = tmp;
  if (!q->head) q->head = tmp;
}

Node* dequeue(Queue *q) {
  q->len--;
  Node *tmp = q->head;
  q->head = q->head->next;
  if (!q->head) q->tail = NULL;
  return tmp;
}

int bfs(int **adj_mt, int V) {
  Queue *q = create_queue();
  int visited[V];
  for (int i = 0; i < V; ++i) visited[i] = 0;
  visited[1] = 1;
  enqueue(q, 1);

  int res = -1;
  for (int i = 0; i < 3; ++i) {
    int len = q->len;
    for (int j = 0; j < len; ++j) {
      int n = dequeue(q)->val;
      res++;
      for (int k = 0; k < V; ++k) {
        if (adj_mt[n][k] && !visited[k]) {
          visited[k] = 1;
          enqueue(q, k);
        }
      }
    }
  }
  return res;
}

int** create_adj_mt(int V) {
  int **mt = (int**)malloc(sizeof(int) * V * V);
  for (int i = 0; i < V; ++i) {
    mt[i] = (int*)malloc(sizeof(int) * V);
    for (int j = 0; j < V; ++j) mt[i][j] = 0;
  }
  return mt;
}

int main() {
  int V, E;
  scanf(" %d %d", &V, &E);
  int** adj_mt = create_adj_mt(V+1);
  int u, v;
  for (int i = 0; i < E; ++i) {
    scanf(" %d %d", &u, &v);
    adj_mt[u][v] = 1;
    adj_mt[v][u] = 1;
  }

  printf("%d", bfs(adj_mt, V));

  return 0;
}
