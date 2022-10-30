#include <iostream>

using namespace std;

#define MAX_NUM 15
typedef struct node *treePointer;
typedef struct node{
    int data;
    treePointer leftChild, rightChild;
}  node;

treePointer Queue[MAX_NUM];
int front = 0, rear = 0;

void Enqueue(treePointer ptr){
    Queue[front++] = ptr;
}
treePointer Dequeue(){
    return Queue[rear++];
}

void preorder(treePointer ptr){
    if(ptr){
        cout << ptr->data << ' ';
        preorder(ptr->leftChild);
        preorder(ptr->rightChild);
    }
}

void inorder(treePointer ptr){
    if(ptr){
        inorder(ptr->leftChild);
        cout << ptr->data << ' ';
        inorder(ptr->rightChild);
    }
}

void postorder(treePointer ptr)
{
    if(ptr){
        postorder(ptr->leftChild);
        postorder(ptr->rightChild);
        cout << ptr->data << ' ';
    }
}

void levelorder(treePointer ptr)
{
    if(!ptr) return;
    Enqueue(ptr);
    while(true){
        ptr = Dequeue();
        if(ptr)
        {
            cout << ptr->data << ' ';
            if(ptr->leftChild)
                Enqueue(ptr->leftChild);
            if(ptr->rightChild)
                Enqueue(ptr->rightChild);
        }
        else
            break;
    }

}

int main()
{
    node nodes[MAX_NUM+1];
    for(int i=1; i<=MAX_NUM; ++i)
    {
        nodes[i].data = i;
        nodes[i].leftChild = NULL;
        nodes[i].rightChild = NULL;
    }

    for(int i=1; i<=MAX_NUM; ++i)
    {
        if(i%2 == 0)
            nodes[i/2].leftChild = &nodes[i];
        else
            nodes[i/2].rightChild = &nodes[i];
    }

    cout << "Preorder : ";
    preorder(&nodes[1]);
    cout << "\n";
    cout << "Inorder : ";
    inorder(&nodes[1]);
    cout << "\n";
    cout << "Postorder : ";
    postorder(&nodes[1]);
    cout << "\n";
    cout << "Levelorder : ";
    levelorder(&nodes[1]);
    cout << "\n";
    return 0;
}