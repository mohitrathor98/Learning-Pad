/*
    Left rotate array by one
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    int size;
    cout<<"Array Size: ";
    cin>>size;

    int arr[size];
    cout<<"Array Elements: ";
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }

    int temp = arr[0];
    for(int i=0;i<size-1;i++){
        arr[i] = arr[i+1];
    }
    arr[size-1] = temp;

    for(int i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}