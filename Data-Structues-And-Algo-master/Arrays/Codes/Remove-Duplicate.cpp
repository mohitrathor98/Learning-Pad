/*
    Remove duplicates from sorted array
*/

#include <bits/stdc++.h>
using std::cin;
using std::cout;

int main(){

    int n;
    cout<<"Size of array: ";
    cin>>n;

    int arr[n];
    cout<<"Elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int size = 1;
    for(int i=1;i<n;i++){
        if(arr[i] != arr[i-1]){
            arr[size] = arr[i];
            size++;
        }
    }

    for(int i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
    cout<<std::endl;

    return 0;
}