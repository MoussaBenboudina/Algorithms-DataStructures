#include <iostream>
#include <stack>
using namespace std;


int main() {

    stack<int> myStack;
    string input;
    int number;

    while(true) {
        cout << "Do you want to add another number? (yes/no): ";
        cin >> input;

        if (input == "yes") {
            cout << "Enter a number: ";
            cin >> number;
            myStack.push(number);
            cout << "Added: " << number << endl;
        } else if (input == "no") {
            break;
        } else {
            cout << "Invalid input. Please enter 'yes' or 'no'." << endl;
        }
    }

    cout << "top element: " << myStack.top() << endl;

     myStack.pop();

    cout << "top element after pop: " << myStack.top() <<endl;

    cout << "Stack size: " << myStack.size() <<endl;

    if (myStack.empty()) {
        cout << "stack is empty." << endl;
    } else {
        cout << "Sack is not empty." << endl;
    }



    return 0;
}
