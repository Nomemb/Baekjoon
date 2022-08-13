#include <iostream>
#include <string>
#include <list>

using namespace std;

int main()
{
    string s;
    int M;

    cin >> s;
    cin >> M;

    list<char> editor(s.begin(), s.end());
    auto cursor = editor.end();

    for (int i = 0; i < M; ++i)
    {
        char cmd;
        cin >> cmd;
        if(cmd == 'L')
        {
            if(cursor != editor.begin()){
                cursor--;
            }
        }
        else if(cmd == 'D')
        {
            if(cursor != editor.end()){
                cursor++;
            }
        }
        else if(cmd == 'B')
        {
            if(cursor != editor.begin())
            {
                cursor--;
                cursor = editor.erase(cursor);
            }
        }
        else if(cmd == 'P')
        {
            char c;
            cin >> c;
            editor.insert(cursor,c);
        }
    }

    for(auto loop: editor)
    {
        cout << loop;
    } 
}