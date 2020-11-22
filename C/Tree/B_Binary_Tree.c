// Problem B

#include <stdio.h>
#include <stdlib.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))

typedef struct Node {
  int val;
  struct Node *left, *right;
} Node;

Node* create_node(int val) {
  Node* res = (Node*)malloc(sizeof(Node));
  res->val = val;
  res->left = res->right = NULL;
  return res;
}

Node* create_BT(int arr[], int i, int n) {
  Node* root = NULL;
  if (i <= n && arr[i-1] != -1) {
    root = create_node(arr[i-1]);
    root->left = create_BT(arr, 2*i, n);
    root->right = create_BT(arr, 2*i+1, n);
  }
  return root;
}

int find_min(Node* root) {
  if (!root) return ~0U >> 1;
  return MIN(root->val, MIN(find_min(root->left), find_min(root->right)));
}

int main(int argc, char *argv[]) {
  int N, tmp;
  scanf(" %d", &N);

  int arr[N];

  for (int i = 0; i < N; ++i) {
    scanf(" %d", &tmp);
    arr[i] = tmp;
  }

  Node* root = create_BT(arr, 1, N);
  printf("%d", find_min(root));
  return 0;
}
