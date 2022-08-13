#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int N, K;
    scanf("%d %d",&N,&K);
    queue<int> queue;
    for(int i=1; i<=N; ++i)
    {
        queue.push(i);
    }
    for(int i=1; i<K; ++i)
    {
        queue.push(queue.front());
        queue.pop();
    }
    cout << "<" << queue.front();
    queue.pop(); 
    while(!queue.empty())
    {
        int k = 1;
        while(k < K)
        {
            queue.push(queue.front());
            queue.pop();
            k++;
        }
        cout <<", " << queue.front();
        queue.pop();
    }
    cout << ">";
}