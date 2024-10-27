#include <iostream>
#include <vector>
using namespace std;

int binarySearch (vector<int> arr , int target);

int main()
{
    vector<int> arr = {10,20,25,30,55,80,12};
    const int target1 = 80;
    const int target2 = 14;

     binarySearch(arr , target1); // output  5
     binarySearch(arr , target2); // output -1;
    return 0;
}


int binarySearch (vector<int> arr , int target) {
    int left = 0;
    int right = arr.size() - 1;

    while(left < right) {
        int mid = (left + right) / 2;
        if(arr[mid] == target) {
            return mid;
        } else if (target > arr[mid]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;

}
