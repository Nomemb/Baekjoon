// https://www.acmicpc.net/problem/2447

#include <iostream>

using namespace std;
void Solve(int n, int y, int x)
{
    if((y/n)%3 == 1 && (x/n)%3 == 1)
    {
        cout << ' ';
    }
    else
    {
        if(n/3 == 0)
        {
            cout << '*';
        }
        else
        {
            Solve(n/3,y,x);
        }
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;

    
    for(int i=0; i < N; ++i)
    {
        for(int j=0;j < N;++j)
        {
            Solve(N,i,j);
        }
        cout << "\n";
    }
    return 0;
}