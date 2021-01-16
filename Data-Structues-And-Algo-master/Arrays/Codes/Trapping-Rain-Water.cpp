/*
    Explanation: https://www.geeksforgeeks.org/trapping-rain-water/

    Input:
    N = 6
    arr[] = {3,0,0,2,0,4}
    Output: 10

    Input:
    N = 4
    arr[] = {7,4,0,9}
    Output: 10
    Explanation: Water trapped by above 
    block of height 4 is 3 units and above 
    block of height 0 is 7 units. So, the 
    total unit of water trapped is 10 units.

    Input:
    N = 3
    arr[] = {6,9,9}
    Output: 0
    Explanation: No water will be trapped.
*/
#include<bits/stdc++.h>
using namespace std;

int min(int a,int b){
    return (a<b)?a:b;
}

int trappingWater(int arr[], int n){

    // Your code here
    int lmax[n],rmax[n];
    // calculate lmax
    int max = arr[0];
    for(int i=0;i<n;i++){
        if(max < arr[i]){
            max = arr[i];
        }
        lmax[i] = max;
    }
    
    //calculate rmax
    max = arr[n-1];
    for(int i=n-1;i>=0;i--){
        if(max < arr[i]){
            max = arr[i];
        }
        rmax[i] = max;
    }
    
    //Amount of water that can be stored: min(rmax[i],lmax[i]) - arr[i]
    int water = 0;
    for(int i=1;i<n-1;i++){
        int diff = min(rmax[i],lmax[i]) - arr[i];
        if(diff>0){
            water += diff;
        }
    }

    return water;
}

int main(){

    int n;
    cout<<"Array Size: ";
    cin>>n;

    int arr[n];
    cout<<"Array Elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    
    cout<<"Trapped Water: "<<trappingWater(arr,n)<<endl;
    
    return 0;
}