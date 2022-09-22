#include <iostream>
using namespace std;

class Set
{
    struct Node
    {
        Node(int data = 0, Node* parent = nullptr, Node* left = nullptr, Node* right = nullptr);
        Node(const Node&) = delete;
        Node& operator=(const Node&) = delete;
        ~Node() = default;

        int Data = 0;
        Node* Parent = nullptr;
        Node* Left = nullptr;
        Node* Right = nullptr;
    };

    public:
        ~Set();

        // 트리의 높이
        int height() const;  // 큐 이용
        int height2() const; // 재귀 이용

        bool empty() const;
        // 트리의 크기 반환
        size_t size() const;

        void clear();
        // 트리에 값 삽입
        bool insert(int value);

        // 트리에서 값 삭제
        void erase(int value);
        void erase(Node* pos);

        // 트리에서 값 찾기
        Node* find(int value) const;

        // 순회
        void traverseByPreorder() const;   // 전위순회
        void traverseByInorder() const;    // 중위순회
        void traverseByPostorder() const;  // 후위순회
        void traverseByLevelorder() const; // 층별순회

    private:
        void traverseByPreorderHelper(Node* node) const;
        void traverseByInorderHelper(Node* node) const;
        void traverseByPostorderHelper(Node* node) const;

        int heightHelper(Node* node) const;

    private:
        Node* _head = new Node();
        size_t _size = 0;
};