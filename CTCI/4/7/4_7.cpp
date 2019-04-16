#include "Graph.h"

int main(void)
{
  try {
    std::vector<char> arr = {'a', 'b', 'c', 'd', 'e', 'f'};
    Graph<char>* graph = new Graph<char>(arr);  
    graph->InsertEdge('a', 'd');
    graph->InsertEdge('f', 'b');
    graph->InsertEdge('b', 'd');
    graph->InsertEdge('f', 'a');
    graph->InsertEdge('d', 'c');
    std::vector<char> build_order = graph->BuildOrder();
    for (size_t i = 0; i < build_order.size(); ++i) {
      std::cout << build_order[i] << " ";
    }

    return 0;
  } catch (Graph<char>::Error e) {
    e.PrintMsg();
  }
}
