package trees;

import nodes.BinaryNode;

public class BinarySearchTree extends BinaryTree<Integer> {
  private BinaryNode<Integer> root;

  public BinarySearchTree(int data) { super(data); }

  public BinaryNode<Integer> searchNode(int val) {
    BinaryNode<Integer> foundNode = searchNodeHelper(root, val); 
    return (foundNode == null) ? null : foundNode;
  }

  public void addNode(int val) { root = addNodeHelper(root, val); }

  public void removeNode(int val) { root = removeNodeHelper(root, val); }

  private BinaryNode<Integer> searchNodeHelper(BinaryNode<Integer> root, int val) {
    if (root.getData() == val) return root;
    if (root.getData() > val) return searchNodeHelper(root.getLeft(), val);
    else return searchNodeHelper(root.getRight(), val);
  }

  private BinaryNode<Integer> addNodeHelper(BinaryNode<Integer> root, int val) {
    if (root == null) return new BinaryNode<Integer>(val);
    if (root.getData() > val) root.setLeft(addNodeHelper(root.getLeft(), val));
    else root.setRight(addNodeHelper(root.getRight(), val));
    return root;
  }

  private BinaryNode<Integer> removeNodeHelper(BinaryNode<Integer> root, int val) {
    if (root == null) return null;
    if (root.getData() == val) {
      if (root.getLeft() == null) return root.getRight();
      if (root.getRight() == null) return root.getLeft();
      BinaryNode<Integer> next = getSuccessor(root.getRight());
      root.setData(next.getData());
      root.setRight(removeNodeHelper(root.getRight(), root.getRight().getData()));
    }
    if (root.getData() > val) root.setLeft(removeNodeHelper(root.getLeft(), val));
    else root.setRight(removeNodeHelper(root.getRight(), val));
    return root;
  }

  private BinaryNode<Integer> getSuccessor(BinaryNode<Integer> root) {
    if (root.getLeft() == null) return root;
    return getSuccessor(root.getLeft());
  }
}
