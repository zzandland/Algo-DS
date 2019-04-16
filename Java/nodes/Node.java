package nodes;

public class Node<T> {
  protected T data;

  public Node(T data) { this.data = data; }

  public T getData() { return this.data; }

  public void setData(T data) { this.data = data; }
}
