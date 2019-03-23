package graphs;

import java.util.Queue;
import java.util.ArrayList;
import java.util.LinkedList;

public class AdjList {
  int numVertices;
  ArrayList<ArrayList<Integer>> edges;
  
  public AdjList(int v) {
    numVertices = v;
    edges = new ArrayList<ArrayList<Integer>>();
    for (int i = 0; i < numVertices; i++) {
      edges.add(new ArrayList<Integer>());
    }
  }

  public void setEdge(int from, int to) {
    edges.get(from).add(to);
  }

  public ArrayList<ArrayList<Integer>> getEdges() {
    return edges;
  }

  public ArrayList<Integer> DST(int start) {
    boolean[] check = new boolean[numVertices];
    ArrayList<Integer> output = new ArrayList<Integer>();
    DSTHelper(start, output, check);
    return output;
  }

  private void DSTHelper(int vertex, ArrayList<Integer> list, boolean[] check) {
    list.add(vertex);
    check[vertex] = true;
    for (int adj : edges.get(vertex)) {
      if (!check[adj]) DSTHelper(adj, list, check);
    }
  }

  public ArrayList<Integer> BST(int start) {
    boolean[] check = new boolean[numVertices];
    Queue<Integer> queue = new LinkedList<>();
    ArrayList<Integer> output = new ArrayList<Integer>();
    queue.add(start);
    check[start] = true;
    while (!queue.isEmpty()) {
      int target = queue.poll();
      output.add(target);
      check[target] = true;
      for (int i = 0; i < edges.get(target).size(); i++) {
        int adj = edges.get(target).get(i);
        if (!check[adj]) queue.add(adj);
      }
    }
    return output;
  }
}
