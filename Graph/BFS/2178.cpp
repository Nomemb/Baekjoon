#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int graph[101][101];
void bfs(int x, int y)
{
    int dx[] = {0,0,-1,1};
    int dy[] = {-1,1,0,0};
    queue<pair<int,int>> queue;
    queue.push({x,y});

    while(!queue.empty())
    {
        x = queue.front().first;
        y = queue.front().second;

        queue.pop();
        for(int i=0;i<4;++i)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(graph[nx][ny] == 1)
            {
                graph[nx][ny] = graph[x][y] + 1;
                queue.push({nx,ny});
            }
        }
    }
}
int main()
{
    int N,M;
    cin >> N >> M;
    for(int i=0; i<N; ++i)
    {
        string s;
        cin >> s;
        for(int j=0; j<M; ++j)
        {
            graph[i][j] = s[j]-'0';
        }
    }
    bfs(0,0);
    cout << graph[N-1][M-1];
}