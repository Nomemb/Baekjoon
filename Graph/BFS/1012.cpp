#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int map[51][51];
bool visited[51][51];
int T,M,N,K;
int x,y;

void bfs(int y, int x)
{
    int dy[] = {-1,1,0,0};
    int dx[] = {0,0,-1,1};
    map[y][x] = 0;
    queue<pair<int,int>> queue;
    queue.push({y,x});

    while(!queue.empty())
    {
        y = queue.front().first;
        x = queue.front().second;
        queue.pop();
        visited[y][x] = true;
        for(int i=0; i<4; ++i)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(0 <= ny && ny < N && 0 <= nx && nx < M)
            {
                if(map[ny][nx] == 1 && !visited[ny][nx])
                {
                    queue.push({ny,nx});
                    visited[ny][nx] = true;
                }
            }
        }
    }
}


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    for(int i=0; i<T; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            for(int w=0; w<M; ++w)
            {
                map[j][w] = 0;
                visited[j][w] = false;
            }
        }
        cin >> M >> N >> K;
        int cnt = 0;
        for(int j=0; j<K; ++j)
        {
            cin >> x >> y;
            map[y][x] = 1;
        }
        for(int y=0; y<N; ++y)
        {
            for(int x=0; x<M; ++x)
            {
                if(map[y][x] == 1 && visited[y][x] == false)
                {
                    cnt++;
                    bfs(y,x);
                }
            }
        }
        cout << cnt << "\n";
    }
}