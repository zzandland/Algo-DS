#include "Graph.h"

int main(void)
{
  try {
    std::vector<char> arr = {'a', 'b', 'c', 'd', 'e', 'f'};
    Graph<char>* graph = new Graph<char>(arr);  

    graph->InsertEdge('b', 'd');
    graph->InsertEdge('d', 'c');
    graph->InsertEdge('f', 'e');
    graph->InsertEdge('e', 'a');
    graph->InsertEdge('e', 'a');
    graph->InsertEdge('a', 'b');
    std::vector<char> path = graph->FullPath();

    for (size_t i = 0; i < path.size(); ++i) {
      std::cout << path[i] << " ";
    }

    return 0;
  } catch (Graph<char>::Error e) {
    e.PrintMsg();
  }
}
