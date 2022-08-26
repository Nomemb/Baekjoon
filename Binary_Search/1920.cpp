#include <iostream>
#include <algorithm>

using namespace std;

bool Binary_Search(int *arr, int size, int value)
{
    int start = 0;
    int end = size;
    while(start < end)
    {
        int mid = start + (end - start) / 2;
        if(arr[mid] == value)
        {
            return true;
        }
        else if(arr[mid] > value)
        {
            end = mid;
        }
        else
        {
            start = mid + 1;
        }
    }
    return false;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;
    int arr[N];
    for(int i=0; i<N; ++i)
    {
        cin >> arr[i];
    }
    sort(arr,arr+N);

    int M;
    cin >> M;
    for(int i=0; i<M; ++i)
    {
        int x;
        cin >> x;
        cout << (Binary_Search(arr,N,x)? 1:0) << "\n";
    }
}

