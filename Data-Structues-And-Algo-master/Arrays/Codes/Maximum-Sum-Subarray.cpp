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

    // Max sum subarray = max(max(maxSumTill(i-1+arr[i],arr[i]))
    int maxSum = 0;
    int curSum = 0;
    for(int i=0;i<n;i++){
        curSum += arr[i];
        if (maxSum < curSum){
            maxSum = curSum;
        } 
    }

    cout<<"Maximum Sum in Given Subarray: "<<maxSum<<endl;

    return 0;
}