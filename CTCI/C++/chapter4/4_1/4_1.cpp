#include "Adj_Graph.h"

int main(void) {
  try {
    Graph<int> *graph = new Graph<int>();
    graph->AddVertex(0);
    graph->AddVertex(1);
    graph->AddVertex(2);
    graph->AddVertex(3);
    graph->AddVertex(4);
    graph->AddVertex(5);

    graph->AddEdge(0, 1);
    graph->AddEdge(0, 4);
    graph->AddEdge(0, 5);
    graph->AddEdge(1, 3);
    graph->AddEdge(1, 4);
    graph->AddEdge(2, 1);
    graph->AddEdge(3, 2);
    graph->AddEdge(3, 4);

    if (graph->RouteBetweenNodes(1, 0))
      std::cout << "Route exists" << std::endl;
    else
      std::cout << "No route." << std::endl;

  } catch (Error e) {
    e.print();
  }

  return 0;
}
