// Question D

#include <stdio.h>
#include <stdlib.h>

#define swap(x, y) do { int tmp = x; x = y; y = tmp; } while (0)

typedef struct {
  int size;
  int cap;
  int *arr;
} Heap;

int parent(int i) { return (i-1) / 2; }

Heap* create_heap(int cap) {
  Heap* hp = (Heap*)malloc(sizeof(Heap));
  hp->size = 0;
  hp->cap = cap;
  hp->arr = malloc(sizeof(int) * cap);
  return hp;
}

void delete_heap(Heap *hp) {
  free(hp->arr);
  free(hp);
}

void heapify(Heap* hp, int i) {
  int l = 2*i + 1;
  int r = 2*i + 2;
  int res = i;

  if (l < hp->size && hp->arr[l] > hp->arr[res]) res = l;
  if (r < hp->size && hp->arr[r] > hp->arr[res]) res = r;
  if (res != i) {
    swap(hp->arr[i], hp->arr[res]);
    heapify(hp, res);
  }
}

void heappush(Heap* hp, int val) {
  if (hp->size < hp->cap) {
    int i = hp->size++;
    hp->arr[i] =  val;
    while (i != 0 && hp->arr[parent(i)] < hp->arr[i]) {
      swap(hp->arr[parent(i)], hp->arr[i]);
      i = parent(i);
    }
  }
}

// if heap is empty return 0
int heappop(Heap* hp) {
  int res;
  if (hp->size > 0) {
    res = hp->arr[0];
    swap(hp->arr[0], hp->arr[hp->size-1]);
    hp->size--;
    heapify(hp, 0);
  } else {
    res = 0;
  }
  return res;
}

int main() {
  int N, tmp;
  scanf(" %d", &N);
  Heap* hp = create_heap(N);

  for (int i = 0; i < N; ++i) {
    scanf(" %d", &tmp);
    if (tmp == 0) printf("%d ", heappop(hp));
    else heappush(hp, tmp);
  }

  delete_heap(hp);
  
  return 0;
}
