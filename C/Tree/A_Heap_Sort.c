// Question A

#include <stdio.h>
#include <stdlib.h>

#define swap(x, y) do { typeof(x) tmp = x; x = y; y = tmp; } while (0)

void heapify(int hp[], int i, int N) {
  int l = 2*i + 1;
  int r = 2*i + 2;
  int t = i;

  if (l < N && hp[l] > hp[t]) t = l;
  if (r < N && hp[r] > hp[t]) t = r;
  if (t != i) {
    swap(hp[i], hp[t]);
    heapify(hp, t, N);
  }
}

void sort(int hp[], int N) {
  for (int i = N/2 - 1; i >= 0; --i)
    heapify(hp, i, N);

  for (int i = N-1; i > 0; --i) {
    swap(hp[0], hp[i]);
    heapify(hp, 0, i);
  }
}

int main() {
  int N, tmp;
  scanf(" %d", &N);
  int hp[N];

  for (int i = 0; i < N; ++i) {
    scanf(" %d", &tmp);
    hp[i] = tmp;
  }

  sort(hp, N);

  for (int i = 0; i < N; ++i)
    printf("%d ", hp[i]);

  printf("\n%d", hp[(N-1) / 2]);
  
  return 0;
}
