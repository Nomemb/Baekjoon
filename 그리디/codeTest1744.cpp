#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int main(int argc, char* argv[])
{
    cin >> n;
    vector<int> vec;
    vector<int> zero_vec;
    vector<int> minus_vec;
    for (int i = 0; i < n; ++i)
    {
        int a;
        cin >> a;
        if(a < 0) minus_vec.push_back(a);
        else if(a == 0) zero_vec.push_back(a);
        else vec.push_back(a);
    }
    sort(vec.rbegin(), vec.rend());
    sort(minus_vec.begin(), minus_vec.end());
    
    long answer = 0;
    const int vec_size = static_cast<int>(vec.size());
    const int minus_vec_size = static_cast<int>(minus_vec.size());
    int zero_vec_size = static_cast<int>(zero_vec.size());
    
    for(int i=0; i<vec_size; i+=2)
    {
        if(i+1 == vec_size)
        {
            answer += vec[i];
        }
        else
        {
            answer += (vec[i]*vec[i+1] > vec[i]+vec[i+1])? vec[i]*vec[i+1] : vec[i]+vec[i+1];
        }
    }
    for(int i=0; i<minus_vec_size; i+=2)
    {
        if(i+1 == minus_vec_size)
        {
            if(zero_vec_size > 0)
            {
                zero_vec_size--;
            }
            else
            {
                answer += minus_vec[i];
            }
        }
        else
        {
            answer += minus_vec[i]*minus_vec[i+1];
        }
    }
    cout << answer;
    return 0;
}
