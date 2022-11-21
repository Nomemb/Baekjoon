#include <iostream>
#include <set>

using namespace std;

int main()
{
    set<int> s;
    s.insert(5);
    s.insert(3);
    s.insert(6);
    s.insert(-1);
    s.insert(10);

    for(set<int>::iterator it = s.begin(); it != s.end(); ++it){
        cout << *it << "\n";
    }
    return 0;
}