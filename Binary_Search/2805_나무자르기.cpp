#include <iostream>
#include <algorithm>

using namespace std;

int solve(int *arr, int size, int value, int max)
{
    long long start,end,mid,ans;
    start = 1;
    end = max;
    ans = 0;
    while(start <= end)
    {
        mid = start + (end - start) / 2;
        long long count = 0;
        for(int i=0; i<size; ++i)
        {
            if(arr[i] - mid >= 0)
            {
                count += arr[i] - mid;
            }
        }
        if(count >= value)
        {
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
    }
    return end;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N,M;
    int max = 0;
    cin >> N >> M;

    int arr[N];
    for(int i=0;i<N;++i)
    {
        cin >> arr[i];
        if(max < arr[i])
        {
            max = arr[i];
        }               
    }
    cout << solve(arr, N, M, max);
}