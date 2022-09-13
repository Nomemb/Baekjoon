#include <iostream>

using namespace std;

void solve(int n)
{
    if(n < 1) return;
    solve(n/2);
    cout << n%2;
}
int main()
{
    int n;
    cin >> n;

    solve(n);
}