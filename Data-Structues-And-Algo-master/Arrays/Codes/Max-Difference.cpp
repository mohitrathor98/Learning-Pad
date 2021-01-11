/*
    Max difference between two elements in an array, arr[i]-arr[j] is max such that i<j
*/

#include<bits/stdc++.h>
using namespace std;

bool isGreater(int first,int second){
    if(first>second){
        return true;
    }
    return false;
}

int main(){

    int n;
    cout<<"Size of array: ";
    cin>>n;

    int arr[n];
    cout<<"Elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int leastElement = arr[0]; int maxDiff = 0;
    for(int j=1;j<n;j++){
        int diff = arr[j] - leastElement;
        if(isGreater(diff,maxDiff)){
            maxDiff = diff;
        }
        if(isGreater(leastElement,arr[j])){
            leastElement = arr[j];
        }
    }
    cout<<"Max-Difference = "<<maxDiff<<endl;
    return 0;
}