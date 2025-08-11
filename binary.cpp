#include <iostream>
using namespace std;

int main() {
    int n, target;

    // Step 1: Get array size
    cout << "Enter the number of elements in the sorted array: ";
    cin >> n;

    int arr[n];

    // Step 2: Get sorted array elements
    cout << "Enter " << n << " elements in sorted (ascending) order:\n";
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Step 3: Get target value
    cout << "Enter the element to search: ";
    cin >> target;

    // Step 4: Binary Search with step-by-step output
    int low = 0, high = n - 1, step = 1;
    bool found = false;

    cout << "\nStarting Binary Search Iterations:\n";
    while (low <= high) {
        int mid = (low + high) / 2;
        cout << "Step " << step << ": low=" << low << ", high=" << high << ", mid=" << mid
             << " → arr[mid] = " << arr[mid] << endl;

        if (arr[mid] == target) {
            cout << "\nElement found at index " << mid << endl;
            found = true;
            break;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
        step++;
    }

    // Step 5: If not found
    if (!found) {
        cout << "\nElement not found in the array.\n";
    }

    return 0;
}
8