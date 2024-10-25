#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void BubbleSort(vector<int>& arr) {
    const int n = arr.size();
    for(int i = 0; i < n; i++){
        for(int j = 0;  j < n - i -1; j++) {
            if(arr[j] > arr[j + 1]) {
                swap(arr[j] , arr[j + 1]);
            }
        }
    }
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




    return 0;
}


import { useDraggable } from '@dnd-kit/core';

function DraggableItem() {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: 'draggable',
  });

  const style = {
    transform: `translate3d(${transform.x}px, ${transform.y}px, 0)`,
  };

  return (
    <div ref={setNodeRef} style={style} {...listeners} {...attributes}>
      Drag me!
    </div>
  );
}
