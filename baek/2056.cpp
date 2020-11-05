#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
  int N;
  cin >> N;
  vector<vector<int>> incom(10001, vector<int>());
  int time[N+1], total[N+1], indegree[N+1];

  for (int i = 0; i < N+1; ++i) time[i] = indegree[i] = 0;

  for (int u = 1; u < N+1; ++u) {
    int t, cnt, v;
    cin >> t >> cnt;
    time[u] = total[u] = t;
    indegree[u] = cnt;
    for (int i = 0; i < cnt; ++i) {
      cin >> v;
      incom[v].push_back(u);
    }
  }

  queue<int> q;
  for (int i = 1; i < N+1; ++i) {
    if (!indegree[i]) q.emplace(i);
  }

  int res, cur;
  res = 0;

  while (!q.empty()) {
    cur = q.front();
    q.pop();

    for (int nxt : incom[cur]) {
      total[nxt] = max(total[nxt], time[nxt] + total[cur]);
      if (!--indegree[nxt]) q.emplace(nxt);
    }
  }

  for (int i = 1; i < N+1; ++i) {
    res = max(res, total[i]);
  }

  cout << res << endl;

  return 0;
}
