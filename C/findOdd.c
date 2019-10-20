#include <stdio.h>

void printBinary(int n) {
  int bitArr[32] = {0};
  int i = 0;
  while (n > 0) {
    bitArr[i++] = n % 2;
    n >>= 1;
  }
  for (i = 31; i >= 0; --i)
    printf("%d", bitArr[i]);
  printf("\n");
}

int findOdd(int* arr, int n) {
  int res = 0, i;
  for (i = 0; i < n; ++i) {
    printBinary(res);
    res ^= arr[i];
  }
  return res;
}

int main(void) {
  int arr[7] = {12, 12, 14, 90, 14, 14, 14};
  printf("%d", findOdd(arr, 7));
  return 0;
}
