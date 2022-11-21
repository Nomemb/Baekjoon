#include <iostream>
#include <string>

using namespace std;
int N,M;
string S;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    cin >> M;
    cin >> S;
    int cnt = 0;
    for(int i=0;i<M-2;++i)
    {
        if(S[i] == 'O') continue;
        else
        {
            int k = 0;
            while(S[i+1] == 'O' && S[i+2] == 'I')
            {
                k++;
                if(k == N)
                {
                    k--;
                    cnt++;
                }
                i += 2;
            }
        }
    }
    cout << cnt;
    
    return 0;
}