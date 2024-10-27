#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isValid(vector<int>& weight, vector<int>& x, int W);
vector<int> sortIndices(const vector<int>& arr);
vector<int> greedyAlgorithm(vector<int>& weight, vector<int>& values, vector<int>& x, int W);
void printArray(const vector<int>& arr);

int main() {
    vector<int> weight = {15, 40, 10, 30};
    vector<int> values = {30, 80, 10, 50};
    vector<int> x(weight.size(), 0);
    int W = 80;

    vector<int> result = greedyAlgorithm(weight, values, x, W);
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

vector<int> greedyAlgorithm(vector<int>& weight, vector<int>& values, vector<int>& x, int W) {
    const int n = weight.size();
    vector<int> sortedIndices = sortIndices(values);

    for (int i = 0; i < n; i++) {
        x[sortedIndices[i]] = 1;
        if (!isValid(weight, x, W)) {
            x[sortedIndices[i]] = 0; 
        }
    }
    return x;
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

vector<int> sortIndices(const vector<int>& arr) {
    const int n = arr.size();
    vector<int> indices(n);

    for (int i = 0; i < n; ++i) {
        indices[i] = i;
    }

    sort(indices.begin(), indices.end(), [&](int a, int b) {
        return arr[a] > arr[b]; 
    });

    return indices;
}
