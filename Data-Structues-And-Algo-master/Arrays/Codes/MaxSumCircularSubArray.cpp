/*
    Maximum sum of subarray which include ciracular subarrays

    [5,-2,3,4] --> 12 
    [8,-4,3,-5,4] --> 12
    [1,2,3,-4] --> 6

    Idea: Maximum of following:
            1) Maximum of Normal Subarray(Kadane's algorithm)
            2) Maximum of circular subarray
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout<<"Size of array: ";
    cin>>n;

    int arr[n];
    cout<<"Array Elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    // find max of normal subarray
    int maxSubarray = 0, currSum = 0;
    for(int i=0;i<n;i++){
        currSum = max(currSum+arr[i],arr[i]);
        maxSubarray = max(maxSubarray,currSum);
    }

    // find max of circular subarray: find min of normal subarray and substract it from total sum of the array
    int totalSum = 0;
    for(int i=0;i<n;i++){
        totalSum += arr[i];
    }

    int minSum = arr[0];
    for(int i=1;i<n;i++){
        currSum = min(currSum+arr[i],arr[i]);
        minSum = min(minSum,currSum);
    }
    int circularMaxSum = totalSum - minSum;

    maxSubarray = max(maxSubarray,circularMaxSum);

    cout<<"Maximum Sum: "<<maxSubarray<<endl;

    return 0;
}