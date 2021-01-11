/*
    Frequency of elements in a sorted array
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    int size;
    cout<<"Size of array: ";
    cin>>size;

    int arr[size];
    cout<<"Sorted elements: ";
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }

    int count = 1;
    cout<<arr[0]<<" ";
    for(int i=1;i<size;i++){
        if(arr[i] != arr[i-1]){
            cout<<count<<"\n"<<arr[i]<<" ";
            count = 1;
        } else {
            count++;
        }
    }
    cout<<count<<endl;

    return 0;
}