#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int t,n;
int main(int argc, char* argv[])
{
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> n;
        int count = 0;
        vector<pair<int,int>> applicant;
        for (int j = 0; j < n; ++j)
        {
            int a,b;
            cin >> a >> b;
            applicant.emplace_back(a,b);
        }
        sort(applicant.begin(), applicant.end());
        int maxValue = applicant[0].second;
        for (const auto value : applicant)
        {
          if(value.second <= maxValue)
          {
              maxValue = value.second;
              count++;
          }
        }
        cout << count << "\n";
    }
    return 0;
}
