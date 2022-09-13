// https://www.acmicpc.net/problem/2606
// 바이러스

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> graph[101];
bool visited[101];
int n,m;
int u,v;
int cnt = 0;
void dfs(int node)
{
    visited[node] = true;
    for(int next : graph[node])
    {
        if(visited[next] == false)
        {
            cnt++;
            dfs(next);
        }
    }
}
int main()
{
    cin >> n;
    cin >> m;
    for(int i = 1; i <= m; ++i)
    {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    for(int i = 1; i <= n; ++i)
    {
        sort(graph[i].begin(), graph[i].end());
    }
    dfs(1);
    cout << cnt << "";
}