// https://www.acmicpc.net/problem/24444
// 너비우선탐색 1

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

vector<int> graph[100001];
int visited[100001];
int cnt = 0;
int N,M,R;
int u,v;
void bfs(int node)
{
    queue<int> queue;
    queue.push(node);
    cnt++;
    visited[node] = cnt;

    while(!queue.empty())
    {
        int i = queue.front();
        queue.pop();
        for(int next : graph[i])
        {
            if(visited[next] == 0)
            {
                queue.push(next);
                cnt++;
                visited[next] = cnt;
            }
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
        sort(graph[i].begin(), graph[i].end());
    }
    bfs(R);
    for(int i = 1; i <= N; ++i)
    {
        cout << visited[i] << "\n";
    }
}
