/*
    N = 7
    A[] = {100,180,260,310,40,535,695}
    Output: (0 3) (4 6)
    Explanation: We can buy stock on day 
                 0, and sell it on 3rd day, which will 
                 give us maximum profit. Now, we buy 
                 stock on day 4 and sell it on day 6.

    N = 5
    A[] = {4,2,2,2,4}
    Output: (3 4)
    Explanation: We can buy stock on day 
                 3, and sell it on 4th day, which will 
                 give us maximum profit.
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
    
    bool buy = false;
   
    for(int i=0;i<n-1;i++){
        if(buy == true){
            if(arr[i+1]<arr[i]){
                buy = false;
                cout<<","<<i<<")"<<" ";
            }
        } else {
            if(arr[i+1]>arr[i]){
                buy = true;
                cout<<"("<<i;
            }
        }
    }
    if(buy == true){
        cout<<","<<n-1<<")";
    }
    cout<<endl;
    return 0;
}