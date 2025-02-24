#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <vector>
#define pp pair<string, int>

using namespace std;

map<string, int> mapset;

bool cmp(const pp& p1, const pp& p2)
{
    if (p1.second == p2.second) return p1.first < p2.first;
    return p1.second > p2.second;
}

vector<string> split(string input, char delimiter)
{
    vector<string> answer;
    stringstream ss(input);
    string temp;

    while (getline(ss, temp, delimiter))
    {
        answer.push_back(temp);
    }
    return answer;
}
int main()
{
    int n;
    cin >> n;
    string names[n];

    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;

        mapset[s] = 0;
    }
    // 공백 제거
    cin.ignore();

    for (int i = 0; i < n; i++)
    {
        string word;
        getline(cin, word);
        vector<string> v = split(word, ' ');

        for (auto & iter : v)
        {
            mapset[iter]++;
        }
    }

    vector<pair<string, int>> orderVec( mapset.begin(), mapset.end() );
    sort(orderVec.begin(), orderVec.end(), cmp);

    for (auto num : orderVec)
    {
        cout << num.first << " " << num.second << endl;
    }
}


/*
참고할 코드

#include <stdio.h>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

char buff[128];
unordered_map<string, int> mp;
pair<int, string> res[128];

int main(void) {
    int n, rsz = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", buff);
        mp.insert({ buff, 0 });
    }
    while (scanf("%s", buff) != EOF) mp[buff]++;
    for (auto& i : mp) {
        res[rsz].first = -i.second;
        res[rsz++].second = i.first;
    }
    sort(res, res + rsz);
    for (int i = 0; i < rsz; i++) {
        printf("%s %d\n", res[i].second.c_str(), -res[i].first);
    }
    return 0;
}
 */