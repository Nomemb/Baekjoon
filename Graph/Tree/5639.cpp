#include <iostream>

using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
};

Node* insert(Node* node, int data){
    if(node == nullptr){
        node = new Node();
        node->data = data;
        node->left = node->right = nullptr;
    }
    else if(data <= node->data){
        node->left = insert(node->left, data);
    }
    else{
        node->right = insert(node->right, data);
    }
    return node;
}

void postorder(Node* node)
{
    if(node->left != nullptr){
        postorder(node->left);
    }
    if(node->right != nullptr){
        postorder(node->right);
    }
    cout << node->data << "\n";
}

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int value;
    Node* root = nullptr;
    while(cin >> value)
    {
        if(value == EOF) break;
        root = insert(root, value);
    }
    postorder(root);
    return 0;
}
