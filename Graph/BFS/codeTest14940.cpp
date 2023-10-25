#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

struct Point
{
    int x;
    int y;
    Point()
    {
        x = 0;
        y = 0;
    }
    Point(int x, int y)
    {
        this->x = x;
        this->y = y;
    }
};


int n,m;
int graph[1000][1000];

int answer[1000][1000];
int dx[] = {0,0,-1,1};
int dy[] = {1,-1,0,0};
Point goal;

void Bfs(Point p, int distance)
{
    
    queue<pair<Point, int>> q;
    q.push(make_pair(p,0));

    while(!q.empty())
    {
        const Point cur = q.front().first;
        const int dist = q.front().second;
        q.pop();


        for(int i=0; i<4; ++i)
        {
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];

            if(nx >= 0 && nx < n && ny >= 0 && ny < m && answer[nx][ny] == -1 && graph[nx][ny] != 0)
            {
                answer[nx][ny] = answer[cur.x][cur.y] + 1;
                q.push(make_pair(Point(nx,ny), dist+1));
            }
        }
    }
}
int main(int argc, char* argv[])
{
    cin >> n >> m;
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            cin >> graph[i][j];
            answer[i][j] = -1;
            if(graph[i][j] == 2)
            {
                goal.x = i;
                goal.y = j;
                answer[i][j] = 0;
            }
        }
    }

    Bfs(goal,0);
    
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            if(graph[i][j] == 0) answer[i][j] = 0;
            cout << answer[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
