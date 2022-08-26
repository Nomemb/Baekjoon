// https://www.acmicpc.net/problem/11729
#include <iostream>

using namespace std;
void Hanoi(int n, int first, int second, int third)
{
    if(n == 1)
    {
        cout << first << " " << third << "\n";
    }
    else
    {
        Hanoi(n-1,first,third,second);
        cout << first << " " << third << "\n";
        Hanoi(n-1,second,first,third);
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;

    cout << (1<<N)-1 << "\n";
    Hanoi(N,1,2,3);
    return 0;
}