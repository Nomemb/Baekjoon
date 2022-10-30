#include <iostream>
#include <algorithm>
#define MAX_ITEMS 100001
using namespace std;

size_t N,x;
size_t numItems = 0;
size_t items[MAX_ITEMS];

void push(int value)
{
    ++numItems;
    items[numItems] = value;

    size_t idx = numItems;
    while (idx != 1 && items[idx / 2] > items[idx]) {
        swap(items[idx / 2], items[idx]);
        idx /= 2;
    }
}
void pop()
{
    if (numItems==0){
        cout << 0 << "\n";
        return;
    }
    size_t ret = items[1];
    cout << ret << "\n";
    size_t parent = 1;
    size_t child = 2;
    items[parent] = items[numItems];
    --numItems;

    while (child <= numItems)
    {
        if (child < numItems && items[child] > items[child + 1])
            child++;

        if (items[parent] <= items[child])
            break;

        swap(items[parent], items[child]);
        parent = child;
        child *= 2;
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for(size_t i=0; i<N; ++i)
    {
        cin >> x;
        if(x == 0) pop();
        else push(x);
    }
    return 0;
}