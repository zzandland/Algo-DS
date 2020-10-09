#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
  int T, V, E, u, v, t, n;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> V >> E;
    int time[V];
    int indegree[V];
    int total[V];
    for (int i = 0; i < V; ++i) {
      cin >> time[i];
      indegree[i] = total[i] = 0;
    }

    unordered_map<int, vector<int>> adj;
    for (int i = 0; i < E; ++i) {
      cin >> u >> v;
      adj[u].emplace_back(v);
      indegree[v-1] += 1;
    }
    cin >> t;
    queue<int> q;
    for (int i = 0; i < V; ++i) {
      if (!indegree[i]) {
        q.emplace(i+1);
      }
    }

    while (!q.empty()) {
      n = q.front();
      q.pop();
      if (n == t) break;
      for (int nn : adj[n]) {
        total[nn-1] = max(total[nn-1], total[n-1] + time[n-1]);
        if (!--indegree[nn-1]) q.emplace(nn);
      }
    }

    cout << total[t-1] + time[t-1] << '\n';
  }
}
