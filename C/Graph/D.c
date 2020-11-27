#include <stdio.h>
#include <stdlib.h>

typedef int coord[2];

typedef struct Node {
  coord crd;
  struct Node *next;
} Node;

Node* create_node(coord crd) {
  Node* node = (Node*)malloc(sizeof(Node));
  node->crd[0] = crd[0];
  node->crd[1] = crd[1];
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

void enqueue(Queue *q, coord crd) {
  q->len++;
  Node *tmp = create_node(crd);
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

int** create_matrix(int h, int w) {
  int **mt = (int**)malloc(sizeof(int) * h * w);
  for (int i = 0; i < h; ++i) mt[i] = malloc(sizeof(int) * w);
  return mt;
}

void delete_matrix(int **mt, int h) {
  for (int i = 0; i < h; ++i) free(mt[i]);
  free(mt);
}

coord dir[] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int bfs(int **mt, int h, int w) {
  Queue *q = create_queue();
  mt[0][0] = 0;
  coord s = {0, 0};
  enqueue(q, s);
  int res = 0;
  int found = 0;
  int y, x, ny, nx;

  while (q->len) {
    int len = q->len;
    res++;
    for (int i = 0; i < len; ++i) {
      Node* out = dequeue(q);
      y = out->crd[0], x = out->crd[1];
      if (y == h-1 && x == w-1) {
        found = 1;
        break;
      }
      for (int j = 0; j < 4; ++j) {
        ny = y + dir[j][0], nx = x + dir[j][1];
        if (0 <= ny && ny < h && 0 <= nx && nx < w && mt[ny][nx] == 1) {
          mt[ny][nx] = 0;
          coord nc = {ny, nx};
          enqueue(q, nc);
        }
      }
    }
  }
  delete_queue(q);
  return found ? res : -1;
}

int main() {
  int w, h, t;
  scanf(" %d %d", &h, &w);
  int** mt = create_matrix(h, w);

  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      scanf("%1d", &t);
      mt[i][j] = t;
    }
  }
  
  printf("%d", bfs(mt, h, w));
  delete_matrix(mt, h);

  return 0;
}
