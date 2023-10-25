#include <iostream>
#include <vector>
#include <queue>
#include <cstdlib>

using namespace std;

int n,l,r;
int map[51][51];
int init_map[51][51];
bool visited[51][51];

int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};

int day = 0;
bool flag = false;
struct Point
{
    int x;
    int y;

    Point(const int x, const int y)
    {
        this->x= x;
        this->y= y;
    }
};
void Bfs(Point cur)
{
    queue<Point> q;
    vector<Point> union_country;
    int sum_union = 0;
    sum_union += map[cur.x][cur.y];
    
    visited[cur.x][cur.y] = true;
    q.push(cur);

    while(!q.empty())
    {
        const auto front = q.front();
        union_country.push_back(front);
        q.pop();
        for (int i = 0; i < 4; ++i)
        {
            const int nx = front.x + dx[i];
            const int ny = front.y + dy[i];

            if(nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny])
            {
                const int diff = abs(map[nx][ny] - map[front.x][front.y]);
                if(diff >= l && diff <= r)
                {
                    flag = true;
                    visited[nx][ny] = true;
                    q.push(Point(nx,ny));
                    sum_union += map[nx][ny];
                }
            }
        }        
    }

    const int avg = sum_union / union_country.size();
    for (const auto country : union_country)
    {
        map[country.x][country.y] = avg;
    }
}
int main(int argc, char* argv[])
{
    cin >> n >> l >> r;
    for (int i = 0; i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
        {
            cin >> map[i][j];
            init_map[i][j] = map[i][j];
        }
    }

    int count = 0;
    while(true)
    {
        flag = false;
        for (int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                if(!visited[i][j])
                {
                    const auto p = Point(i,j);
                    Bfs(p);
                }
            }
        }

        for (int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                //map[i][j] = init_map[i][j];
                visited[i][j] = false;
            }
        }

        if(!flag)
        {
            cout << count;
            break;
        }
        count++;
    }

    return 0;
}
