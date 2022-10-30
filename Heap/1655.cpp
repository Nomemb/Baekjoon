#include <iostream>
#include <algorithm>
#define MAX_ITEMS 100001
using namespace std;

int N,x;
int minNumItems = 0;
int maxNumItems = 0;
int minItems[MAX_ITEMS];
int maxItems[MAX_ITEMS];

void minPush(int value)
{
    ++minNumItems;
    minItems[minNumItems] = value;

    int idx = minNumItems;
    while (idx != 1 && minItems[idx / 2] > minItems[idx]) {
        swap(minItems[idx / 2], minItems[idx]);
        idx /= 2;
    }
}

void minPop()
{
    if (minNumItems==0){
        cout << 0 << "\n";
        return;
    }
    int ret = minItems[1];
    int parent = 1;
    int child = 2;
    minItems[parent] = minItems[minNumItems];
    --minNumItems;

    while (child <= minNumItems)
    {
        if (child < minNumItems && minItems[child] > minItems[child + 1])
            child++;

        if (minItems[parent] <= minItems[child])
            break;

        swap(minItems[parent], minItems[child]);
        parent = child;
        child *= 2;
    }
}
void maxPush(int value)
{
    ++maxNumItems;
    maxItems[maxNumItems] = value;

    int idx = maxNumItems;
    while (idx != 1 && maxItems[idx / 2] < maxItems[idx]) {
        swap(maxItems[idx / 2], maxItems[idx]);
        idx /= 2;
    }
}


void maxPop()
{
    if (maxNumItems==0){
        cout << 0 << "\n";
        return;
    }
    int ret = maxItems[1];
    int parent = 1;
    int child = 2;
    maxItems[parent] = maxItems[maxNumItems];
    --maxNumItems;

    while (child <= maxNumItems)
    {
        if (child < maxNumItems && maxItems[child] < maxItems[child + 1])
            child++;

        if (maxItems[parent] >= maxItems[child])
            break;

        swap(maxItems[parent], maxItems[child]);
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
    for(int i=0; i<N; ++i)
    {
        cin >> x;
        if(maxNumItems > minNumItems) minPush(x);
        else maxPush(x);

        if(maxNumItems != 0 && minNumItems != 0)
        {
            if(maxItems[1] > minItems[1])
            {
                int a = maxItems[1];
                int b = minItems[1];

                maxPop();
                minPop();

                maxPush(b);
                minPush(a);
            }
        }
        cout << maxItems[1] << "\n";
    }
    return 0;
}