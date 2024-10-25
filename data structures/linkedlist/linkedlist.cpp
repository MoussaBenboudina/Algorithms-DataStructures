#include <iostream>
using namespace std;


struct Node {
    int data;
    Node* next;

    Node(int val) : data(val), next(nullptr) {}
};

Node* head = nullptr;

void appendFirst(int val);
void printList();
void appendLast(int val);
void appendByIndex(int val, int index);
void clearList();





int main()
{

    appendFirst(1);
    appendFirst(2);

    appendLast(1);
    appendLast(2);

    appendByIndex(100 , 2);

    printList();
    
 
    clearList();
    return 0;
}







void appendFirst(int val) {
    Node* newNode = new Node(val);

    if(!head) {
        head = newNode;
    } else {
        newNode->next = head;
        head = newNode;
    }

}



void appendLast(int val) {
    Node* newNode = new Node(val);

    if(!head) {
        head = newNode;
    } else {
       Node* dummy = head;
       while(dummy->next != nullptr) {
            dummy = dummy->next;
       }
       dummy->next = newNode;
    }

}


void printList() {
    Node* dummy = head;
    while(dummy != nullptr) {
        cout << dummy->data << " -> " ;
        dummy = dummy->next;
    }
}



void appendByIndex(int val, int index) {
        Node* newNode = new Node(val);

        if(index < 0) {
            cout << "index cannot be negative !" <<endl;
            delete newNode;
            return;
        }

        if(index == 0) {
            delete newNode;
            appendFirst(val);
        }


        Node* current = head;
        int currenIndex = 0;

        while( current != nullptr && currenIndex < index - 1) {
            current = current->next;
            currenIndex++;
        }

        if (current == nullptr) {
            cout << "Index out of bounds. Appending at the end." << endl;
            delete newNode;
            appendLast(val);
            return;
        }


        Node* nextNode = current->next;
        current->next = newNode;
        newNode->next = nextNode;

}



void clearList() {
    Node* current = head;
    while(current != nullptr) {
        Node* nextNode = current->next;
        delete current;
        current = nextNode;
    }
     head = nullptr;
}
