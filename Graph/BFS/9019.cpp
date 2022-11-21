#include <iostream>
#include <queue>

using namespace std;
int T, a, b;

void bfs(int curr, int key)
{
    queue<pair<int, string>> q;
    bool visited[10001] = {};
    q.push({ curr, "" });
    visited[curr] = true;
    
    while (!q.empty())
    {
        curr = q.front().first;
        string currStr = q.front().second;
        q.pop();
        if (curr == key)
        {
            cout << currStr << "\n";
            return;
        }
        pair<int, string> next;
        for (int i = 0; i < 4; ++i)
        {
            if (i == 0)
            {
                next = { (curr * 2) % 10000,"D" };
            }
            else if (i == 1)
            {
                next = { (curr == 0) ? 9999 : (curr - 1),"S" };

            }
            else if (i == 2) {
                next = { (curr % 1000) * 10 + (curr / 1000),"L" };

            }
            else {
                next = { (curr % 10) * 1000 + (curr / 10),"R" };
            }
            if (visited[next.first] == false)
            {
                visited[next.first] = true;
                q.push({ next.first, currStr + next.second });
            }
        }
    }
}
int main()
{
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        cin >> a >> b;
        bfs(a, b);
    }
    return 0;
}