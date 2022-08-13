#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int N;
    scanf("%d",&N);

    queue<int> queue;
    for(int i=1; i<= N; ++i)
    {
        queue.push(i);
    }
    while(queue.size() != 1)
    {
        queue.pop();
        queue.push(queue.front());
        queue.pop();
    }
    cout << queue.front();
}