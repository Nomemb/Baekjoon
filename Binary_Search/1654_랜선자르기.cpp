#include <iostream>
#include <algorithm>

using namespace std;

int solve(int *arr, int size, int value, int max)
{
    long long int start, end, mid;
    start = 1;
    end = max;
    while(start <= end)
    {
        mid = start + (end - start) / 2;
        long long int count = 0;
        for(int i=0; i<size; ++i)
        {
            count += arr[i]/mid;
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

    int K, N;
    cin >> K >> N;
    int arr[K];
    int max = 0;
    for(int i=0;i<K;++i)
    {
        cin >> arr[i];
        if(arr[i] > max)
        {
            max = arr[i];
        }
    }
    cout << solve(arr, K, N, max);
    
}