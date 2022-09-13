// https://www.acmicpc.net/problem/24480
// 알고리즘 수업 2

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> graph[100001];
int visited[100001];
int cnt = 0;
int N,M,R;
int u,v;
void dfs(int node)
{
    cnt += 1;
    visited[node] = cnt;
    
    for(int next : graph[node])
    {
        if(visited[next] == 0)
        {
            dfs(next);
        }
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> R;
    for(int i = 1; i <= M; ++i)
    {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for(int i = 1; i <= N; ++i)
    {
        sort(graph[i].begin(), graph[i].end(), greater<int>());
    }
    dfs(R);
    for(int i = 1; i <= N; ++i)
    {
        cout << visited[i] << "\n";
    }
}
