#include <iostream>
using namespace std;

int linearSearch (vector<int> arr , int target);

int main()
{
    vector<int> arr = {10,20,25,30,55,80,12};
    const int target1 = 20;
    const int target2 = 14;

    linearSearch(arr , target1); // output index 1;
    linearSearch(arr , target2); // output -1;


    return 0;
}



int linearSearch (vector<int> arr , int target) {

    const int n = arr.size();

    for(int i =0; i < n; i++){
        if(arr[i] == target){
            return i;
        }
    }

    return -1;
}
