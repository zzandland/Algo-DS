#include <iostream>
#include <vector>

struct TreeNode {
  int data;
  TreeNode *left;
  TreeNode *right;

  TreeNode(int val) {
    data = val;
    left = right = nullptr;
  }

  virtual ~TreeNode() {
    delete left;
    delete right;
  }
};

class BST {
public:
  virtual ~BST() { delete root_; }

  void insertNode(int val) {
    if (root_ == nullptr)
      root_ = new TreeNode(val);
    else
      insertNode(val, root_);
  }

  void kthSmallest(int k) { kthHelper(k, root_, true); }

  void kthLargest(int k) { kthHelper(k, root_, false); }

  std::vector<int> reverseInorder() {
    std::vector<int> output;
    if (root_ == nullptr)
      return output;
    reverseInorder(root_, output);
    return output;
  }

private:
  TreeNode *root_;

  void kthHelper(int &k, TreeNode *node, bool smallest) {
    if (node == nullptr)
      return;
    if (smallest)
      kthHelper(k, node->left, true);
    else
      kthHelper(k, node->right, false);
    if (--k == 0) {
      std::cout << node->data;
      return;
    }
    if (smallest)
      kthHelper(k, node->right, true);
    else
      kthHelper(k, node->left, false);
  }

  TreeNode *insertNode(int val, TreeNode *node) {
    if (node == nullptr)
      return new TreeNode(val);
    if (node->data > val)
      node->left = insertNode(val, node->left);
    else
      node->right = insertNode(val, node->right);
    return node;
  }

  void reverseInorder(TreeNode *node, std::vector<int> &arr) {
    if (node == nullptr)
      return;
    reverseInorder(node->right, arr);
    arr.push_back(node->data);
    reverseInorder(node->left, arr);
  }
};

int main(void) {
  BST *b = new BST();
  b->insertNode(3);
  b->insertNode(5);
  b->insertNode(7);
  b->insertNode(9);
  b->insertNode(12);
  b->kthSmallest(2);
  std::cout << std::endl;
  b->kthLargest(2);
  delete b;
  return 0;
}
