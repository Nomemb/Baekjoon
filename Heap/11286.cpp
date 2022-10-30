#include <iostream>
#include <algorithm>
#define MAX_ITEMS 100001
using namespace std;

int N,x;
int numItems = 0;
int items[MAX_ITEMS];

bool compare(int a, int  b)
{
    return (abs(a)==abs(b))? a>b : abs(a)>abs(b);
}
void push(int value)
{
    ++numItems;
    items[numItems] = value;

    int idx = numItems;
    while (idx != 1 && (compare(items[idx/2], items[idx]))) {
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
    int ret = items[1];
    cout << ret << "\n";
    int parent = 1;
    int child = 2;
    items[parent] = items[numItems];
    --numItems;

    while (child <= numItems)
    {
        if (child < numItems && (compare(items[child],items[child+1])))
            child++;

        if (!compare(items[parent], items[child]))
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
    for(int i=0; i<N; ++i)
    {
        cin >> x;
        if(x == 0) pop();
        else push(x);
    }
    return 0;
}