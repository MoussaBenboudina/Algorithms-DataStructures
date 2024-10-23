#include <iostream>
#include <vector>
using namespace std;

void swap (int& a , int& b) {
    int temp = a;
           a = b;
           b = temp;
}



void BubbleSort(vector<int>& arr) {

    const int n = arr.size();

    for(int i = 0; i < n; i++)
        for(int j = 0;  j < n - i -1; j++)
            if(arr[j] > arr[j + 1])
                swap(arr[j] , arr[j + 1]);

}

void printArray(vector<int> arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}


int main()
{

    vector<int> arr = {1,4,9,2,0,4,6};
    cout << "before sorting : ";
    printArray(arr);
    BubbleSort(arr);
    cout << "after sorting  : ";
    printArray(arr);



    cout << "Hello world!" << endl;
    return 0;
}
