#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout<<"Size of Array: ";
    cin>>n;

    vector<int> v;
    cout<<"Elements: ";
    for(int i=0;i<n;i++){
        int e;
        cin>>e;
        v.push_back(e);
    }

    int nonZero = 0;
    for(int i=0;i<n;i++){
        if(v[i] != 0){
            swap(v[i],v[nonZero]);
            nonZero++;
        }
    }

    for(int i=0;i<n;i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;

    return 0;
}