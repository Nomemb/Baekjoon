#include <iostream>
#include <list>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;

    list<char> password;
    for (int i = 0; i < T; ++i)
    {
        password.clear();
        string L;
        cin >> L;
        auto cursor = password.begin();
        for (int j = 0; j < L.length(); ++j)
        {
            if(L[j] == '-')
            {
                if( cursor != password.begin())
                {
                    cursor--;
                    cursor = password.erase(cursor);         
                }
            }
            else if(L[j] == '<')
            {
                if(cursor != password.begin())
                {
                    cursor--;
                }
            }
            else if(L[j] == '>')
            {
                if(cursor != password.end())
                {
                    cursor++;
                }
            }
            else
            {
                password.insert(cursor, L[j]);
            }
        }
        for(auto loop : password)
        {
            cout << loop;
        }
        cout << "\n";
    }
    
}