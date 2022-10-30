#include <iostream>

using namespace std;
struct Node{
    char left;
    char right;
};

Node tree[27];
int N;

 
void preorder(char root){
    cout << root;
    if(tree[root].left != '.')
        preorder(tree[root].left);
    if(tree[root].right != '.')
        preorder(tree[root].right);
}

void inorder(char root){
    if(tree[root].left != '.')
        inorder(tree[root].left);
    cout << root;
    if(tree[root].right != '.')
        inorder(tree[root].right);
}

void postorder(char root){
    if(tree[root].left != '.')
        postorder(tree[root].left);
    if(tree[root].right != '.')
        postorder(tree[root].right);
    cout << root;
}

int main()
{
    cin >> N;
    for(int i=0; i<N; ++i)
    {
        char root, left, right;
        cin >> root >> left >> right;
        tree[root].left = left;
        tree[root].right = right;
    }

    preorder('A');
    cout << "\n";
    inorder('A');
    cout << "\n";
    postorder('A');

}