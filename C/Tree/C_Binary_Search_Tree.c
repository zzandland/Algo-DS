// Problem C

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int val;
  struct Node *left, *right;
} Node;

Node* create_node(int val) {
  Node* root = (Node*)malloc(sizeof(Node));
  root->val = val;
  root->left = root->right = NULL;
  return root;
}

Node* insert_node(Node* root, int val) {
  if (!root) return create_node(val);
  if (root->val > val) root->left = insert_node(root->left, val);
  else root->right = insert_node(root->right, val);
  return root;
}

int search(Node* root, int target, int cnt) {
  if (!root || root->val == target) return cnt;
  printf("%d ", root->val);
  if (root->val > target) return search(root->left, target, cnt+1);
  else return search(root->right, target, cnt+1);
}

int main() {
  int N, target, tmp;
  scanf(" %d %d", &N, &target);

  Node* root = NULL;
  
  for (int i = 0; i < N; ++i) {
    scanf(" %d", &tmp);
    root = insert_node(root, tmp);
  }

  int cnt = search(root, target, 0);
  printf("\n%d", cnt);
  return 0;
}
