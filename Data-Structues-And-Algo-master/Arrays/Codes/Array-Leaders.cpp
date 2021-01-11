
#include<bits/stdc++.h>
using namespace std;

void rev(int arr[],int start,int end){
    while(start<end){
        swap(arr[start],arr[end]);
        start++;
        end--;
    }
}

int main(){

    int size;
    cout<<"Array Size: ";
    cin>>size;

    int arr[size];
    cout<<"Elements: ";
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }

    int result[size],count = 0;
    int largest = arr[size-1];
    result[count++] = largest;
    for(int i=size-2;i>=0;i--){
        if(arr[i]>largest){
            largest = arr[i];
            result[count++] = largest;
        }
    }

    rev(result,0,count-1);

    for(int i=0;i<count;i++){
        cout<<result[i]<<" ";
    }
    cout<<endl;

    return 0;
}