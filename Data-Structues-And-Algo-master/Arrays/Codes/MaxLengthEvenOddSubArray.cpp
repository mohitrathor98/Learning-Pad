/*
    Maximum length of subarray with alternating even-odd or odd-even numbers
    [10,12,14,7,8] --> 3
    [7,10,13,14]  --> 4
    [10,12,8,4]   --> 1
*/

#include<bits/stdc++.h>
using namespace std;

bool isEven(int n){
    return (n%2 == 0)?true:false;
}

int main(){

    int size;
    cout<<"Size of array: ";
    cin>>size;

    int arr[size];
    cout<<"Elements: ";
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }

    int preOdd = 0, preEven = 0, longestSubarray = 0, subArray = 0;
    for(int i=0;i<size;i++){
        if(preOdd==0 && preEven==0){
            //first element
            if(isEven(arr[i])){
                preEven = 1;
            } else {
                preOdd = 1;
            }
            subArray++;
        } else if(preEven){
            if(isEven(arr[i])){
                longestSubarray = subArray;
                subArray = 1;
            } else {
                subArray++;
                preOdd = 1;
                preEven = 0;
            }
        } else if(preOdd){
            if(isEven(arr[i])){
                subArray++;
                preOdd = 0;
                preEven = 1;
            } else {
                longestSubarray = subArray;
                subArray = 1;
            }
        }
    }
    if(subArray > longestSubarray){
        longestSubarray = subArray;
    }

    cout<<"Size of longest subarray with alternate odd-even values: "<<longestSubarray<<endl;
    return 0;
}