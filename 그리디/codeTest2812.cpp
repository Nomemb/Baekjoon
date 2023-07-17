// https://www.acmicpc.net/problem/2812

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
    int n, k;
    string numbers;
    cin >> n >> k;
    cin >> numbers;
    vector<int> answer;
    for (const auto value : numbers)
    {
        int num = value-'0';
        if(k == 0 || answer.empty())
        {
            answer.push_back(num);
            continue;
        }

        if(answer.back() < num)
        {
            while(!answer.empty() && answer.back() < num && k > 0)
            {
                answer.pop_back();
                k--;                
            }
        }
        answer.push_back(num);
    }
    for(int i=0; i<answer.size()-k; ++i)
    {
        cout << answer[i];
    }
    return 0;
}
