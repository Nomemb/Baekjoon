/*
https://www.acmicpc.net/problem/17478
����Լ��� ������?
*/

#include <iostream>

using namespace std;
void PrintUnderBar(int count)
{
    for(int i=0; i< count; ++i) cout << "____";
}
void Recursion(int count, int n)
{
    PrintUnderBar(count);
    cout << "\"����Լ��� ������?\"" << "\n";
    if(count == n)
    {
        PrintUnderBar(count);
        cout << "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"" << "\n";
    }
    else
    {
        PrintUnderBar(count);
        cout << "\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���." << "\n";
        PrintUnderBar(count);
        cout << "���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���." << "\n";
        PrintUnderBar(count);
        cout << "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"" << "\n";
        Recursion(count+1,n);
    }
    PrintUnderBar(count);
    cout << "��� �亯�Ͽ���." << "\n";
}
int main()
{
    int N;
    scanf("%d",&N);
    cout << "��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������." << "\n";
    Recursion(0,N);
}