/*
    I/P: N = 7 arr[] = {2,3,-8,7,-1,2,3}
    O/P: 11

    I/P: N = 3 arr[] = {5,8,3}
    O/P: 16

    I/P: N = 3 arr[] = {-6,-1,-8}
    O/P: -1
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

    // Max sum subarray = max(array of max(maxSumTill(i-1)+arr[i],arr[i]))
    int maxSumArray[n];
    int maxSum = 0;
    for(int i=0;i<n;i++){
        maxSumArray[i] = max(maxSum+arr[i],arr[i]); 
        maxSum = maxSumArray[i];
    }
    
    maxSum = maxSumArray[0];
    for(int i=1;i<n;i++){
        if(maxSum < maxSumArray[i]){
            maxSum = maxSumArray[i];
        }
    }

    cout<<"Maximum Sum in Given Subarray: "<<maxSum<<endl;

    return 0;
}