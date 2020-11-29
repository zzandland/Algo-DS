// 숨바꼭질

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

int bfs(int N, int K) {
  Queue *q = create_queue();
  enqueue(q, N);

  int x, len, res = -1;
  while (1) {
    int len = q->len;
    res++;
    for (int i = 0; i < len; ++i) {
      x = dequeue(q)->val;
      if (x == K) {
        delete_queue(q);
        return res;
      }
      enqueue(q, x+1);
      enqueue(q, x-1);
      enqueue(q, x*2);
    }
  }
}

int main() {
  int N, K;
  scanf(" %d %d", &N, &K);

  printf("%d", bfs(N, K));
  
  return 0;
}
