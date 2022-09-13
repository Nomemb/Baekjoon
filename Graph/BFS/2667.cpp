// https://www.acmicpc.net/problem/2667
// 단지번호붙이기

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

char map[26][26];
bool visited[26][26];
int N;
int cnt = 0;
vector<int> vec;
void bfs(int y, int x)
{
    int dy[] = {-1,1,0,0};
    int dx[] = {0,0,-1,1};

    queue<pair<int,int>> queue;
    queue.push({y,x});
    visited[y][x] = true;
    cnt++;

    while(!queue.empty())
    {
        y = queue.front().first;
        x = queue.front().second;
        queue.pop();
        for(int i=0; i<4; ++i)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(0 <= ny && ny < N && 0 <= nx && nx < N)
            {
                if(visited[ny][nx] == false && map[ny][nx] == '1')
                {
                    queue.push({ny,nx});
                    visited[ny][nx] = true;
                    cnt++;
                }
            }

        }
    }
}
int main()
{
    cin >> N;
    for(int i=0; i<N; ++i)
    {
       scanf("%s", map[i]);
    }
    for(int y=0; y<N; ++y)
    {
        for(int x=0; x<N; ++x)
        {
            if(map[y][x] == '1' && visited[y][x] == false)
            {
                cnt = 0;
                bfs(y,x);
                vec.push_back(cnt);
            }
        }
    }
    sort(vec.begin(), vec.end());
    cout << vec.size() << "\n";
    for(int i = 0; i < vec.size(); ++i)
    {
        cout << vec[i] << "\n";
    }
}