package graphs;

import java.util.Hashtable;
import java.util.Arrays;
import java.util.ArrayList;

public class AdjMatrix {
  int numVertex;
  int[][] adjMatrix;
  Hashtable<Character, Integer> vertices = new Hashtable<Character, Integer>();
  char[] verticesList;

  public AdjMatrix(int numVertex) {
    this.numVertex = numVertex;
    this.adjMatrix = new int[numVertex][numVertex];
    for (int[] row : this.adjMatrix) {
      Arrays.fill(row, -1);
    }
    this.verticesList = new char[numVertex];
  }

  public char[] getVertices() {
    return verticesList;
  }

  public Edge[] getEdges() {
    ArrayList<Edge> edgesList = new ArrayList<Edge>();
    for (int i = 0; i < adjMatrix.length; i++) {
      for (int j = 0; j < adjMatrix[i].length; j++) {
        if (adjMatrix[i][j] != -1) edgesList.add(new Edge(verticesList[i], verticesList[j], adjMatrix[i][j]));
      }
    }
    Edge[] edgeArr = new Edge[edgesList.size()];
    edgeArr = edgesList.toArray(edgeArr);
    return edgeArr;
  }

  public int[][] getGraph() {
    return adjMatrix;
  }

  public void setVertex(int id, char vtx) {
    vertices.put(vtx, id);
    verticesList[id] = vtx;
  }

  public void setEdge(char from, char to, int cost) {
    int fromId = vertices.get(from);
    int toId = vertices.get(to);
    adjMatrix[fromId][toId] = cost;
    adjMatrix[toId][fromId] = cost;
  }
}
