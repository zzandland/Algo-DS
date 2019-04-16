package nodes;

public class BinaryCountNode extends BinaryNode<Integer> {
  private int count = 1;
  private BinaryCountNode left, right;

  public BinaryCountNode(int val) { super(val); }

  public BinaryCountNode getLeft() { return left; }

  public void setLeft(BinaryCountNode node) { left = node; }

  public BinaryCountNode getRight() { return right; }

  public void setRight(BinaryCountNode node) { right = node; }

  public int getCount() { return this.count; }

  public void setCount(int val) { this.count = val; }
}
