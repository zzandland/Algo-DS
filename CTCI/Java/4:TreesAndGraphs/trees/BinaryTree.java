package trees;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.function.Consumer;
import nodes.BinaryNode;

public class BinaryTree<T> implements TreeMethods<T> {
  protected BinaryNode<T> root;

  public BinaryTree(T data) { root = new BinaryNode<T>(data); }

  public BinaryNode<T> getRoot() { return root; }

  public ArrayList<T> preorderTraversal() {
    Consumer<ArrayList<T>> func = list -> preorderTraversalHelper(root, list);
    return traversalHelper(func);
  }

  public ArrayList<T> inorderTraversal() {
    Consumer<ArrayList<T>> func = list -> inorderTraversalHelper(root, list);
    return traversalHelper(func);
  }

  public ArrayList<T> postorderTraversal() {
    Consumer<ArrayList<T>> func = list -> postorderTraversalHelper(root, list);
    return traversalHelper(func);
  }

  public ArrayList<T> BreathFirstTraversal() {
    Consumer<ArrayList<T>> func = list -> BreathFirstTraversalHelper(list);
    return traversalHelper(func);
  }

  private ArrayList<T> traversalHelper(Consumer<ArrayList<T>> func) {
    ArrayList<T> list = new ArrayList<T>();
    func.accept(list);
    return list;
  }

  private void preorderTraversalHelper(BinaryNode<T> node, ArrayList<T> list) {
    list.add(node.getData());
    if (node.getLeft() != null) preorderTraversalHelper(node.getLeft(), list);
    if (node.getRight() != null) preorderTraversalHelper(node.getRight(), list);
  }

  private void inorderTraversalHelper(BinaryNode<T> node, ArrayList<T> list) {
    if (node.getLeft() != null) inorderTraversalHelper(node.getLeft(), list);
    list.add(node.getData());
    if (node.getRight() != null) inorderTraversalHelper(node.getRight(), list);
  }

  private void postorderTraversalHelper(BinaryNode<T> node, ArrayList<T> list) {
    if (node.getLeft() != null) postorderTraversalHelper(node.getLeft(), list);
    if (node.getRight() != null) postorderTraversalHelper(node.getRight(), list);
    list.add(node.getData());
  }

  private void BreathFirstTraversalHelper(ArrayList<T> list) {
    BinaryNode<T> node;
    Queue<BinaryNode<T>> queue = new LinkedList<>();
    queue.add(root);    
    while (queue.peek() != null) {
      node = queue.poll();
      list.add(node.getData());
      if (node.getLeft() != null) queue.add(node.getLeft());
      if (node.getRight() != null) queue.add(node.getRight());
    }
  }
}
