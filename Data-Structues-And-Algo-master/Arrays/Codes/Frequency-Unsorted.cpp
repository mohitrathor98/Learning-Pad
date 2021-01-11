/*
    Frequency of elements in an unsorted array
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    int size;
    cout<<"Size of array: ";
    cin>>size;

    int arr[size];
    cout<<"Sorted elements: ";
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }

    
    unordered_map<int,int> m;
    for(int i=0;i<size;i++){
        if(m.find(arr[i]) == m.end()){
            m.insert({arr[i],1});
        } else {
            m[arr[i]]++;
        }
    }

    for(auto i:m){
        cout<<i.first<<" "<<i.second<<endl;
    }

    return 0;
}