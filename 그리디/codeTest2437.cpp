// https://www.acmicpc.net/problem/2437
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n;
vector<int> weights;
int solve()
{
    sort(weights.begin(), weights.end());
    if(weights[0] != 1) return 1;
    int answer = 0;
    
    for (const auto weight : weights)
    {
        if(answer + 1 < weight) return answer+1;

        answer += weight;
    }
    return answer+1;
}
int main(int argc, char* argv[])
{
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int weight;
        cin >> weight;
        weights.push_back(weight);
    }
    const int answer = solve();
    cout << answer;
    return 0;
}
