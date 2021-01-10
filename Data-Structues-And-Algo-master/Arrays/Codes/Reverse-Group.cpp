/*
  N = 5, K = 3
  arr[] = {1,2,3,4,5}
  Output: 3 2 1 5 4  
*/
#include<bits/stdc++.h>
using std::cout;
using std::cin;


int main(){
    int n,k;
    
    cout<<"N = "; cin>>n;
    cout<<"k = "; cin>>k;
    
    int arr[n];
    
    cout<<"Array elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    for(int i=0;i<n;i+=k){
            
        // check if k elements remaining in array
        if((n-i) < k){
            k = (n-i);
        }
            
        // reverse the group from i to next k elements
        int low = i;
        int high = i+k-1;
        while(low<high){
            int temp = arr[low];
            arr[low] = arr[high];
            arr[high] = temp;
            low++;
            high--;
        }
    }


    cout<<"Output: ";
    for(int i = 0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<std::endl;

    return 0;
}