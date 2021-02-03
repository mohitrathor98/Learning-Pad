/*
    5 --> [2,3,2,3,5] O/P: 0 2 2 0 1
    Explanation:
        1 occurs 0 times
        2 occurs 2 times
        3 occurs 2 times
        4 occurs 0 times
        5 occurs 1 times
    
    4 --> [3,3,3,3] O/P: 0 0 4 0
    
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout<<"Array Size: ";
    cin>>n;

    int arr[n];
    cout<<"Array Elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    // substract -1 from each element (due to 0 indexing)
    for(int i=0;i<n;i++){
        arr[i] -= 1;
    }
    
    
    // add n to the element at i%n index
    for(int i=0;i<n;i++){
        arr[arr[i]%n] = arr[arr[i]%n]+n;
    }

    
    // at each index remove n from elements and print number of times n removed
    for(int i=0;i<n;i++){
        arr[i] = arr[i]/n;
    }

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}