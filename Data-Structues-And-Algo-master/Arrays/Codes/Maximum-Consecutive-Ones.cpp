/*
    Maximum Consecutive ones in binary array

    I/P: N = 4 arr = [1,1,0,1]
    O/P: 2

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

    int maxOne = 0;
    int curMax = 0;
    for(int i=0;i<n;i++){
        if(arr[i] == 1){
            curMax++;
        } else {
            if(curMax>maxOne){
                maxOne = curMax;
            }
            curMax = 0;
        }
    }
    if(curMax>maxOne){
        maxOne = curMax;
    }
    cout<<"Maximum consecutive 1 in the given binary array: "<<maxOne<<endl;
    return 0;
}