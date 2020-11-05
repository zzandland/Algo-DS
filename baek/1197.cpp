#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#define P pair<int, int>

using namespace std;

int find(int v, vector<int>& parents) {
  if (v != parents[v]) parents[v] = find(parents[v], parents);
  return parents[v];
}

bool union_(int a, int b, vector<int>& parents) {
  int af = find(a, parents), bf = find(b, parents);
  if (af == bf) return false;
  parents[af] = bf;
  return true;
}

int kruskal(int V, int E) {
  int u, v, w;
  vector<pair<int, P>> edges;

  for (int i = 0; i < E; ++i) {
    cin >> u >> v >> w;
    edges.push_back({w, P(u, v)});
  }

  sort(edges.begin(), edges.end());

  vector<int> parents(V+1);
  for (int i = 1; i < V+1; ++i) parents[i] = i;

  int res = 0;
  for (auto [w, uv] : edges) {
    if (union_(uv.first, uv.second, parents)) res += w;
  }

  return res;
}

int prim(int V, int E) {
  int a, b, c;
  long long res = 0;
  vector<P> edges[10001];
  int seen[10001];

  for (int i = 0; i < E; ++i) {
    cin >> a >> b >> c;
    edges[a].push_back({c, b});
    edges[b].push_back({c, a});
  }

  priority_queue<P, vector<P>, greater<P>> pq;
  pq.push(P(0, 1));

  while (!pq.empty()) {
    auto [w, n] = pq.top();
    pq.pop();

    if (seen[n]) continue;
    seen[n] = 1;
    res += w;

    for (int i = 0; i < edges[n].size(); ++i) {
      if (!seen[edges[n][i].second]) pq.push(edges[n][i]);
    }
  }
  return res;
}

int main(int argc, char *argv[]) {
  int V, E;

  cin >> V >> E;

  cout << prim(V, E);

  return 0;
}
