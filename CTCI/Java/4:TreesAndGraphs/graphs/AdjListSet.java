package graphs;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Queue;
import java.util.LinkedList;

public class AdjListSet {
  int V;
  ArrayList<HashSet<Integer>> edges;

  public AdjListSet(int v) {
    V = v;
    edges = new ArrayList<HashSet<Integer>>(V);
    for (int i = 0; i < V; i++) {
      edges.add(new HashSet<Integer>());
    }
  }

  public void getGraph() {
    for (HashSet<Integer> vertex : edges) {
      System.out.println(vertex);
    }
  }

  public void getEdge(int from, int to) {
    if (edges.get(from).contains(to)) System.out.println(String.format("Edge from %d to %d found", from, to));
    else System.out.println(String.format("Edge from %d to %d not found", from, to));
  }

  public void setEdge(int from, int to) {
    edges.get(from).add(to);
    edges.get(to).add(from);
  }

  public ArrayList<Integer> DFS(int from) {
    boolean[] check = new boolean[V];
    check[from] = true;
    ArrayList<Integer> output = new ArrayList<Integer>();
    DFSHelper(from, output, check);
    return output;
  }

  public ArrayList<Integer> BFS(int from) {
    boolean[] check = new boolean[V];
    check[from] = true;
    ArrayList<Integer> output = new ArrayList<Integer>();
    Queue<Integer> queue = new LinkedList<>();
    queue.add(from);
    int vertex;
    while (!queue.isEmpty()) {
      vertex = queue.poll();
      output.add(vertex);
      Iterator<Integer> iterator = edges.get(vertex).iterator();
      while (iterator.hasNext()) {
        int adj = iterator.next();
        if (!check[adj]) {
          check[adj] = true;
          queue.add(adj);
        }
      }
    }
    return output;
  }

  private void DFSHelper(int vertex, ArrayList<Integer> list, boolean[] check) {
    list.add(vertex);
    Iterator<Integer> iterator = edges.get(vertex).iterator();
    while (iterator.hasNext()) {
      int adj = iterator.next();
      if (!check[adj]) {
        check[adj] = true;
        DFSHelper(adj, list, check);
      }
    }
  }
}
