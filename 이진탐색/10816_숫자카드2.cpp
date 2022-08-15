#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    int arr[N];
    for(int i=0;i<N;++i)
    {
        cin >> arr[i];
    }
    sort(arr,arr+N);
    int M;
    cin >> M;
    for(int i=0;i<M;++i)
    {
        int x;
        cin >> x;
        pair<int*, int*> range = equal_range(arr,arr+N,x);
        cout << range.second - range.first << " ";
    }
}