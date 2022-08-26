// https://www.acmicpc.net/problem/10872

#include <iostream>

using namespace std;

int Factorial(int n, int total = 1)
{
    if(n == 1 || n == 0) return total;
    return Factorial(n-1, n*total);
}
int main()
{
    int N;
    scanf("%d",&N);
    cout << Factorial(N);
    return 0;
}