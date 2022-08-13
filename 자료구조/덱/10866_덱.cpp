#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    deque<int> deque;
    int N;
    cin >> N;
    for(int i=0; i<N; ++i)
    {
        string s;
        cin >> s;
        if(s == "push_front")
        {
            int X;
            cin >> X;
            deque.push_front(X);
        }
        else if(s == "push_back")
        {
            int X;
            cin >> X;
            deque.push_back(X);
        }
        else if(s == "pop_front")
        {
            if(!deque.empty())
            {
                cout << deque.front() << "\n";
                deque.pop_front();
            }
            else
            {
                cout << -1 << "\n";
            }
        }
        else if(s == "pop_back")
        {
            if(!deque.empty())
            {
                cout << deque.back() << "\n";
                deque.pop_back();
            }
            else
            {
                cout << -1 << "\n";
            }
        }
        else if(s == "size")
        {
            cout << deque.size() << "\n";
        }
        else if(s == "empty")
        {
            cout << (deque.empty()? 1:0) << "\n";
        }
        else if(s == "front")
        {
            cout << (deque.empty()? -1:deque.front()) << "\n";
        }
        else if(s == "back")
        {
            cout << (deque.empty()? -1:deque.back()) << "\n";
        }
    }
}