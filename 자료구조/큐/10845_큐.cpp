#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    queue<int> queue;
    int N;
    cin >> N;
    for(int i=0; i<N; ++i)
    {
        string s;
        cin >> s;
        if(s == "push")
        {
            int X;
            cin >> X;
            queue.push(X);
        }
        else if(s == "pop")
        {
            if(!queue.empty())
            {
                cout << queue.front() << "\n";
                queue.pop();
            }
            else
            {
                cout << -1 << "\n";
            }
        }
        else if(s == "size")
        {
            cout << queue.size() << "\n";
        }
        else if(s == "empty")
        {
            cout << (queue.empty()? 1:0) << "\n";            
        }
        else if(s == "front")
        {
            cout << (queue.empty()? -1:queue.front()) << "\n";
        }
        else if(s == "back")
        {
            cout << (queue.empty()? -1:queue.back()) << "\n";
        }
    }
}