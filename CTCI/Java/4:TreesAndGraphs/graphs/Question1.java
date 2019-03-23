package graph;

import java.util.ArrayList;
import java.util.HashMap;

public class Question1<T> {
  private static class GraphNode<T> {
    private T data;
    private ArrayList<GraphNode<T>> children = new ArrayList<GraphNode<T>>();

    public GraphNode(T data) {
      this.data = data;
    }

    public void insertChild(GraphNode<T> child) {
      children.add(child);
    }
  }

  private HashMap<T, Integer> vertices = new HashMap<T, Integer>(); 
  private GraphNode<T>[] verticesList;
  private int size = 0;
  
  public Question1(int limit) {
  }

  public void setVertex(T data) {
    GraphNode<T> newNode = new GraphNode<T>(data);

  }

  public void addEdge(GraphNode<T> from, GraphNode<T> to) {
    from.insertChild(to);    
  }

  public boolean routesBetween(GraphNode<T> from, GraphNode<T> to) {
    return true;
  }
}
