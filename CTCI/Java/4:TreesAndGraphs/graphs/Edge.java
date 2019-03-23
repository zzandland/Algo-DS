package graphs;

public class Edge {
  public final char from;
  public final char to;
  public final int cost;

  public Edge(char from, char to, int cost) {
    this.from = from;
    this.to = to;
    this.cost = cost;
  }
}
