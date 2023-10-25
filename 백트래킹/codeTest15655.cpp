#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m;
vector<int> arr;
vector<int> answer;
bool visited[9];
void Bfs(int length, int depth)
{
    if(depth == length)
    {
        for(int a : answer)
        {
            cout << a << " ";
        }
        cout << "\n";
    }
    else
    {
        for(int i=0; i<n; ++i)
        {
            if(!visited[i])
            {
                if(answer.empty() || arr[i] > answer.back())
                {
                    visited[i] = true;
                    answer.push_back(arr[i]);
                    Bfs(length, depth+1);
                    answer.pop_back();
                    visited[i] = false;
                }
            }
        }
    }
}
int main(int argc, char* argv[])
{
    cin >> n >> m;
    arr.resize(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    Bfs(m,0);
    return 0;
}
