#ifndef GRAPH_H
#define GRAPH_H

#include <iostream>
#include <map>
#include <set>
#include <vector>

template <class T>
class Graph {
 public:
  class Error {
    public:
      std::string msg_;

      Error(std::string msg);
      void PrintMsg();
  };
  Graph(std::vector<T> arr);
  virtual ~Graph();
  void InsertEdge(T from, T to);
  void DeleteEdge(T from, T to);
  std::vector<T> BuildOrder();

 private:
  int size_;
  std::map<T, int> vertex_;
  std::vector<std::vector<bool>> adj_matrix_;
  int GetDependency(T vertex);
};

template <class T>
Graph<T>::Error::Error(std::string msg) {
  msg_ = msg;
}

template <class T>
void Graph<T>::Error::PrintMsg() {
  std::cout << msg_ << std::endl;
}

template <class T>
Graph<T>::Graph(std::vector<T> arr) {
  size_ = arr.size();
  for (int i = 0; i < size_; ++i) {
    vertex_.insert({arr[i], i});
    std::vector<bool> row(size_);
    adj_matrix_.push_back(row);
  }
}

template <class T>
Graph<T>::~Graph() {
  delete this;
}

template <class T>
void Graph<T>::InsertEdge(T from, T to) {
  adj_matrix_[vertex_[from]][vertex_[to]] = true;
}

template <class T>
void Graph<T>::DeleteEdge(T from, T to) {
  adj_matrix_[vertex_[from]][vertex_[to]] = false;
}

template <class T>
std::vector<T> Graph<T>::BuildOrder() {
  std::vector<T> build_order;
  std::vector<T> temp;
  for (auto it = vertex_.begin(); it != vertex_.end(); ++it) {
    temp.push_back(it->first);
  }

  while (temp.size() > 0) {
    size_t i = 0;
    while (i < temp.size()) {
      int dependency_index = GetDependency(temp[i]);
      if (dependency_index == -1) {
        int index = vertex_[temp[i]];
        build_order.push_back(temp[i]);
        temp.erase(temp.begin() + i);
        for (int j = 0; j < size_; ++j) {
          adj_matrix_[index][j] = false;
        }
      } else {
        if (adj_matrix_[i][dependency_index])
          throw Error("There is no valid build order");
        i++;
      }
    }
  }

  return build_order;
}

template <class T>
int Graph<T>::GetDependency(T vertex) {
  for (int i = 0; i < size_; ++i)
    if (adj_matrix_[i][vertex_[vertex]]) return i;
  return -1;
}

#endif /* GRAPH_H */
