#include <iostream>
#include <vector>
using namespace std;

int n,m;
int graph[301][301];
bool visited[301][301];
bool init_visited[301][301];

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

struct Point
{
    int x;
    int y;

    Point(int x,int y)
    {
        this->x = x;
        this->y = y;
    }
};

void InitVisited()
{
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            visited[i][j] = init_visited[i][j];
        }
    }
}

int Dfs(Point p)
{
    visited[p.x][p.y] = true;
    for(int i=0;i<4;++i)
    {
        const int nx = p.x+dx[i];
        const int ny = p.y+dy[i];

        if(nx >= 0 && nx < n && ny >=0 && ny < m && !visited[nx][ny])
        {
            if(graph[nx][ny] != 0)
            {
                Dfs(Point(nx,ny));
            }
        }
    }
    return 1;
}

int CountBlock()
{
    int block_count = 0;
    InitVisited();
        
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            if(graph[i][j] != 0 && !visited[i][j])
            {
                block_count += Dfs(Point(i,j));
            }
        }
    }
    return block_count;
}

void MeltDfs(Point p)
{
    visited[p.x][p.y] = true;
    for(int i=0;i<4;++i)
    {
        const int nx = p.x+dx[i];
        const int ny = p.y+dy[i];

        if(graph[nx][ny] == 0 && !visited[nx][ny])
        {
            graph[p.x][p.y] = (graph[p.x][p.y] - 1 > 0)? graph[p.x][p.y]-1 : 0;
        }
        if(nx >= 0 && nx < n && ny >=0 && ny < m && !visited[nx][ny])
        {
            if(graph[nx][ny] != 0)
            {
                MeltDfs(Point(nx,ny));
            }
        }
    }
}

void Melt()
{
    InitVisited();
        
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            if(graph[i][j] != 0 && !visited[i][j])
            {
                MeltDfs(Point(i,j));
            }
        }
    }
}
int main(int argc, char* argv[])
{
    int answer = 0;
    cin >> n >> m;
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            cin >> graph[i][j];
        }
    }

    int block_count = CountBlock();
    
    while(block_count == 1)
    {
        answer++;
        Melt();
        block_count = CountBlock();
        if(block_count == 0)
        {
            answer = block_count;
        }
    }


    cout << answer;
    return 0;
}
