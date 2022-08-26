// https://www.acmicpc.net/problem/2110

#include <iostream>
#include <algorithm>

using namespace std;
int solve(int *arr, int end, int N, int C)
{
    int ans = 0;
    int distance = 0;
    int start = 1;
    while(start <= end)
    {
        int count = 1;
        distance = arr[0];
        int mid = (start+end)/2;
        for(int i=0; i<N;++i)
        {
            if(arr[i] - distance >= mid)
            {
                count++;
                distance = arr[i];
            }
        }

        if(count >= C)
        {
            ans = (ans<mid? mid:ans);
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
        
    }

    return ans;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int max = 0;
    int N,C;
    cin >> N >> C;
    int arr[N];
    for(int i=0;i<N;++i)
    {
        cin >> arr[i];        
    }
    sort(arr,arr+N);
    cout << solve(arr, arr[N-1]-arr[0], N, C);
}