/*
    Given a sorted array of distinct integers, sort it in a wave like structure:

    5
    1 2 3 4 5

    O/P: 2 1 4 3 5

    6
    2 4 7 8 9 10

    O/P: 4 2 8 7 10 9
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

    for(int i=0;i<n-1;i+=2){
        int temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
    }

    cout<<"Wave array: ";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}