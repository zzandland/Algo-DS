#ifndef ADJ_GRAPH_H
#define ADJ_GRAPH_H

#include <map>
#include <set>
#include <vector>
#include "Queue.h"

template <class T>
class Graph {
 public:
  class Node {
   public:
    T data_;
    bool visited_;
    std::vector<Node*> children_;

    Node(T data);

    ~Node() { delete this; };
  };

  Graph(){};

  ~Graph() { delete this; };

  void AddVertex(T vertex);

  void RemoveVertex(T target);

  void AddEdge(T from, T to);

  void RemoveEdge(T from, T to);

  void printVertices() {
    for (size_t i = 0; i < vertices_.size(); ++i) {
      std::cout << vertices_[i]->data_ << " ";
    }
    std::cout << std::endl;
  }

  void IterateEdge(T target);

  bool RouteBetweenNodes(T from, T to);

 private:
  std::vector<Node*> vertices_;
};

template <class T>
Graph<T>::Node::Node(T data) {
  data_ = data;
  visited_ = false;
  children_ = std::vector<Node*>();
}

template <class T>
void Graph<T>::AddVertex(T vertex) {
  Node* new_node = new Node(vertex);
  vertices_.push_back(new_node);
}

template <class T>
void Graph<T>::RemoveVertex(T target) {
  for (size_t i = 0; i < vertices_.size(); ++i) {
    if (vertices_[i]->data_ == target) vertices_.erase(vertices_.begin() + i);
  }
}

template <class T>
void Graph<T>::AddEdge(T from, T to) {
  Node* from_node = nullptr;
  Node* to_node = nullptr;
  for (size_t i = 0;
       (from_node == nullptr || to_node == nullptr) && i < vertices_.size();
       ++i) {
    Node* curr_node = vertices_[i];
    if (curr_node->data_ == from) {
      from_node = curr_node;
    }
    if (curr_node->data_ == to) {
      to_node = curr_node;
    }
  }

  if (to_node == nullptr) to_node = new Node(from);
  from_node->children_.push_back(to_node);
}

template <class T>
void Graph<T>::RemoveEdge(T from, T to) {
  for (size_t i = 0; i < vertices_.size(); ++i) {
    if (vertices_[i]->data_ == from) {
      std::vector<Node*> from_node_adj = vertices_[i]->children_;
      for (size_t j = 0; j < from_node_adj.size(); ++j) {
        if (from_node_adj[j]->data_ == to) {
          from_node_adj.erase(from_node_adj.begin() + j);
        }
      }
    }
  }
}

template <class T>
void Graph<T>::IterateEdge(T target) {
  for (size_t i = 0; i < vertices_.size(); ++i) {
    if (vertices_[i]->data_ == target) {
      std::vector<Node*> target_adj = vertices_[i]->children_;
      for (size_t j = 0; j < target_adj.size(); ++j) {
        std::cout << target_adj[j]->data_ << " ";
      }
      std::cout << std::endl;
      return;
    }
  }
}

template <class T>
bool Graph<T>::RouteBetweenNodes(T from, T to) {
  Node* from_node;
  for (size_t i = 0; i < vertices_.size(); ++i) {
    if (vertices_[i]->data_ == from) {
      from_node = vertices_[i];
    }
  }
  if (from_node == nullptr) return false;

  Queue<Node*> *q = new Queue<Node*>();
  Node* n;
  q->Enqueue(from_node);

  while (!q->Empty()) {
    n = q->Top();
    q->Dequeue();
    if (n->data_ == to) return true;
    n->visited_ = true;
    std::vector<Node*> adj = n->children_;
    for (size_t i = 0; i < adj.size(); ++i) {
      if (!adj[i]->visited_) q->Enqueue(adj[i]);
    }
  }
  return false;
}

#endif /* ADJ_GRAPH_H */
