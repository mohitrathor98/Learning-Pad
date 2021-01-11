/*
    Left rotate an array by d
*/
#include<bits/stdc++.h>
using namespace std;

void rev(int arr[],int start,int end){
    while(start<end){
        swap(arr[start],arr[end]);
        start++;
        end--;
    }
}

int main(){

    int size;
    cout<<"Array Size: ";
    cin>>size;

    int arr[size];
    cout<<"Elements: ";
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }

    int d;
    cout<<"Left Rotate by(d): ";
    cin>>d;

    rev(arr,0,d-1);
    rev(arr,d,size-1);
    rev(arr,0,size-1);

    for(int i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}