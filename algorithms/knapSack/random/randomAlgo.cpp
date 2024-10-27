#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isValid(vector<int>& weight, vector<int>& x, int W);
void printArray(const vector<int>& arr);
vector<int> random(vector<int>& weight, vector<int>& x, int W);


int main() {
    vector<int> weight = {15, 40, 10, 30};
    vector<int> values = {30, 80, 10, 50};
    vector<int> x(weight.size(), 0);
    int W = 80;

    vector<int> result =  random(weight, x, W);
    printArray(result);

    return 0;
}

bool isValid(vector<int>& weight, vector<int>& x, int W) {
    int s = 0;
    for (size_t i = 0; i < weight.size(); ++i) {
        s += x[i] * weight[i];
    }
    return s <= W;
}


vector<int> random(vector<int>& weight, vector<int>& x, int W) {

    const int n = x.size();

    while(1) {
        for(int i = 0; i < n; i++){
        x[i] = rand() % 2;
        }

        if(isValid(weight , x , W)) {
            return x;
        }
    }


}



void printArray(const vector<int>& arr) {
    cout << "[";
    for (size_t i = 0; i < arr.size(); ++i) {
        cout << arr[i];
        if (i < arr.size() - 1) {
            cout << ",";
        }
    }
    cout << "]" << endl;
}