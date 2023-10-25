#include <iostream>
using namespace std;

int n,k;
int weight[51];
bool visited[51];
int threeExercise = 500;
int answer = 0;
void Bfs(int day)
{
    if(day == n)
    {
        answer++;
        return;
    }

    for(int i=0; i<n; ++i)
    {
        if(!visited[i])
        {
            if(threeExercise + weight[i] >= 500)
            {
                threeExercise += weight[i];
                visited[i] = true;
                Bfs(day + 1);
                threeExercise -= weight[i];
                visited[i] = false;                
            }
            
        }
    }
}
int main(int argc, char* argv[])
{
    cin >> n >> k;
    for(int i=0; i<n; ++i)
    {
        cin >> weight[i];
        weight[i] -= k;
    }
    Bfs(0);
    cout << answer;
    return 0;
}
