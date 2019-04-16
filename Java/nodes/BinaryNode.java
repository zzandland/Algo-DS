package nodes;

public class BinaryNode<T> extends Node<T> {
  protected BinaryNode<T> left, right;

  public BinaryNode(T data) { super(data); }

  public BinaryNode<T> getLeft() { return this.left; }

  public void setLeft(BinaryNode<T> node) { this.left = node; }

  public BinaryNode<T> getRight() { return this.right; }

  public void setRight(BinaryNode<T> node) { this.right = node; }
}
