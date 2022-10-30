#include <iostream>
#include <vector>

using namespace std;

vector<int> graph[100001];
int parent[100001];
int N;

void SetParent(int p, int c)
{
    parent[c] = p;
    for(int _c : graph[c])
    {
        if(parent[_c] == 0)
        {
            SetParent(c, _c);
        }
    }
}
int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0; i<N-1; ++i)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    SetParent(1,1);

    for(int i=2; i<=N; ++i)
    {
        cout << parent[i] << "\n";
    }
}