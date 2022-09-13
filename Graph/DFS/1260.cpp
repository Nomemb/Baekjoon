// https://www.acmicpc.net/problem/1260
// DFS BFS

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

vector<int> graph[1001];
bool visited[1001];
int N,M,R;
int u,v;
void dfs(int node)
{
    visited[node] = true;
    cout << node << " ";
    
    for(int next : graph[node])
    {
        if(visited[next] == false)
        {
            dfs(next);
        }
    }
}

void bfs(int node)
{
    fill_n(visited,1001,false);
    queue<int> queue;
    queue.push(node);
    visited[node] = true;

    while(!queue.empty())
    {
        int i = queue.front();
        cout << i << " ";
        queue.pop();
        
        for(int next : graph[i])
        {
            if(visited[next] == 0)
            {
                queue.push(next);
                visited[next] = true;
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

    dfs(R);
    cout << "\n";
    bfs(R);
}