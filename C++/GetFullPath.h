#ifndef GRAPH_H
#define GRAPH_H

#include <iostream>
#include <vector>

template <class T>
class Graph {
  class Node {
   public:
    T data_;
    std::vector<Node*> adj_;
    bool visited_;

    Node(T data);
  };

 public:
  class Error {
   public:
    std::string msg_;

    Error(std::string msg);
    void PrintMsg();
  };

  Graph();
  Graph(std::vector<T> arr);
  virtual ~Graph();
  void InsertVertex(T data);
  void DeleteVertex(T data);
  void InsertEdge(T from, T to);
  void DeleteEdge(T from, T to);
  std::vector<T> FullPath();

 private:
  std::vector<Node*> vertices_;
  void GetVertices(T from, T to, Node*& from_node, Node*& to_node);
  void FullPathHelper(Node* node, std::vector<T>& arr, bool& found);
};

template <class T>
Graph<T>::Node::Node(T data) {
  data_ = data;
  visited_ = false;
}

template <class T>
Graph<T>::Error::Error(std::string msg) {
  msg_ = msg;
}

template <class T>
void Graph<T>::Error::PrintMsg() {
  std::cout << msg_ << std::endl;
}

template <class T>
Graph<T>::Graph() {}

template <class T>
Graph<T>::Graph(std::vector<T> arr) {
  for (size_t i = 0; i < arr.size(); ++i) InsertVertex(arr[i]);
}

template <class T>
Graph<T>::~Graph() {}

template <class T>
void Graph<T>::InsertVertex(T data) {
  Node* n = new Node(data);
  vertices_.push_back(n);
}

template <class T>
void Graph<T>::DeleteVertex(T data) {
  for (size_t i = 0; i < vertices_.size(); ++i) {
    if (vertices_[i]->data_ == data) {
      vertices_.erase(vertices_.begin() + i);
      return;
    }
  }
}

template <class T>
void Graph<T>::InsertEdge(T from, T to) {
  Node* from_node = nullptr;
  Node* to_node = nullptr;
  GetVertices(from, to, from_node, to_node);

  if (from_node == nullptr || to_node == nullptr)
    throw Graph::Error("Both nodes must exist in the graph to create an edge");

  from_node->adj_.push_back(to_node);
}

template <class T>
void Graph<T>::DeleteEdge(T from, T to) {
  Node* from_node = nullptr;
  Node* to_node = nullptr;
  GetVertices(from, to, from_node, to_node);

  if (from_node == nullptr || to_node == nullptr)
    throw Graph::Error("Both nodes must exist in the graph to create an edge");

  std::vector<Node*> from_node_adj = from_node->adj_;

  for (size_t i = 0; i < from_node_adj->size(); ++i) {
    if (from_node_adj[i] == to_node)
      from_node_adj.erase(from_node_adj->begin() + i);
    return;
  }
}

template <class T>
void Graph<T>::GetVertices(T from, T to, Node*& from_node, Node*& to_node) {
  for (size_t i = 0; i < vertices_.size(); ++i) {
    Node* curr_node = vertices_[i];
    if (curr_node->data_ == from)
      from_node = curr_node;
    else if (curr_node->data_ == to)
      to_node = curr_node;

    if (from_node != nullptr && to_node != nullptr) return;
  }
}

template <class T>
std::vector<T> Graph<T>::FullPath() {
  std::vector<T> arr;
  bool found = false;

  for (size_t i = 0; i < vertices_.size(); ++i) {
    FullPathHelper(vertices_[i], arr, found);
    if (found) {
      return arr;
    } else {
      for (size_t j = 0; j < vertices_.size(); ++j) {
        vertices_[j]->visited_ = false;
      }
      arr.clear();

      std::cout << std::endl;
    }
  }

  throw Graph::Error("There is no path between the vertices.");
}

template <class T>
void Graph<T>::FullPathHelper(Node* node, std::vector<T>& arr, bool& found) {
  arr.push_back(node->data_);
  node->visited_ = true;

  if (arr.size() == vertices_.size()) {
    found = true;    
    return;
  }

  std::vector<Node*> node_adj = node->adj_;

  for (size_t i = 0; i < node_adj.size(); ++i) {
    if (!node_adj[i]->visited_) {
      FullPathHelper(node_adj[i], arr, found);
      if (found) break;
      arr.pop_back();
    }
  }
}

#endif /* GRAPH_H */
